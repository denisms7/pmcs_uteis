from django.shortcuts import render
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from PyPDF2 import PdfMerger
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from PyPDF2 import PdfReader, PdfWriter
from django.http import HttpResponse, HttpResponseRedirect
import os
import zipfile
from .forms import PDFUploadForm, SplitPDFForm
import shutil
import uuid


def merge_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_files = request.FILES.getlist('pdf_files')
            fs = FileSystemStorage()
            uploaded_files = []
            for pdf_file in pdf_files:
                # Gera um nome único para o arquivo usando UUID
                file_name = f"{uuid.uuid4()}.pdf"
                uploaded_file = fs.save(file_name, pdf_file)
                uploaded_files.append(fs.path(uploaded_file))

            # Realiza o merge dos arquivos
            output_filename = f"merged_pdf_{timezone.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            output_path = os.path.join(settings.MEDIA_ROOT, output_filename)
            merge_files(uploaded_files, output_path)

            # Cria a resposta para download do arquivo mesclado
            with open(output_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{output_filename}"'

            # Remove os arquivos temporários
            for uploaded_file in uploaded_files:
                os.remove(uploaded_file)

            # Move o arquivo mesclado para a pasta de mídia
            shutil.move(output_path, os.path.join(settings.MEDIA_ROOT, output_filename))

            # Armazena o caminho do arquivo mesclado na sessão
            request.session['merged_pdf_path'] = os.path.join(settings.MEDIA_ROOT, output_filename)

            # Chama a função para excluir o arquivo mesclado após o download
            delete_merged_pdf(output_filename)

            return response
    else:
        form = PDFUploadForm()

    return render(request, 'pdf_ferramentas/merge.html', {'form': form})


def delete_merged_pdf(merged_pdf_filename):
    merged_pdf_path = os.path.join(settings.MEDIA_ROOT, merged_pdf_filename)
    if os.path.exists(merged_pdf_path):
        os.remove(merged_pdf_path)
        return True
    return False

def merge_files(files, output_path):
    merger = PdfMerger()
    for file in files:
        merger.append(file)
    merger.write(output_path)
    merger.close()

# ======================================================================

def split_pdf(request):
    if request.method == 'POST':
        form = SplitPDFForm(request.POST, request.FILES)

        if form.is_valid():
            pdf_files = request.FILES.getlist('pdf_file')  # Acessar os arquivos enviados

            # Gerar um identificador exclusivo para a sessão atual
            session_id = str(uuid.uuid4())

            # Criar um diretório temporário para armazenar os arquivos PDF separados
            temp_dir = os.path.join(settings.MEDIA_ROOT, 'split_pdf_temp', session_id)
            os.makedirs(temp_dir, exist_ok=True)

            # Separar os arquivos PDF e salvar as páginas individuais
            pdf_paths = []
            for pdf_file in pdf_files:
                pdf_path = os.path.join(temp_dir, pdf_file.name)
                with open(pdf_path, 'wb') as output_file:
                    pdf_reader = PdfReader(pdf_file)
                    num_pages = len(pdf_reader.pages)
                    for page_number in range(num_pages):
                        output_filename = f'page_{page_number + 1}.pdf'
                        output_path = os.path.join(temp_dir, output_filename)
                        pdf_writer = PdfWriter()
                        pdf_writer.add_page(pdf_reader.pages[page_number])
                        with open(output_path, 'wb') as page_file:
                            pdf_writer.write(page_file)
                        pdf_paths.append(output_path)

            # Criar o arquivo ZIP
            zip_filename = f'split_pdf_{session_id}.zip'
            zip_path = os.path.join(settings.MEDIA_ROOT, zip_filename)
            zip_file = zipfile.ZipFile(zip_path, 'w')

            # Adicionar as páginas individuais ao ZIP
            for pdf_path in pdf_paths:
                zip_file.write(pdf_path, os.path.basename(pdf_path))

            zip_file.close()

            # Remover o diretório temporário
            shutil.rmtree(temp_dir)

            # Redirecionar para a URL de download do arquivo ZIP
            download_url = reverse('download_zip', args=[session_id])
            return HttpResponseRedirect(download_url)

    else:
        form = SplitPDFForm()

    return render(request, 'pdf_ferramentas/split.html', {'form': form})



def download_zip(request, session_id):
    zip_filename = f'split_pdf_{session_id}.zip'
    zip_path = os.path.join(settings.MEDIA_ROOT, zip_filename)

    # Criar a resposta HTTP para o download do arquivo ZIP
    with open(zip_path, 'rb') as zip_file:
        response = HttpResponse(zip_file.read(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(zip_filename)

    # Excluir o arquivo ZIP após o download
    os.remove(zip_path)

    return response

