from django import forms
from multiupload.fields import MultiFileField

def validate_pdf(value):
    for file in value:
        if not file.name.lower().endswith('.pdf'):
            raise forms.ValidationError('Por favor, selecione apenas arquivos PDF.')

# =================================


class PDFUploadForm(forms.Form):
    pdf_files = MultiFileField(
        min_num=2,
        max_num=50,
        max_file_size=1024*1024*100,  # 100MB
        required=True,
        label='Selecione os arquivos PDF',
        error_messages={'min_num': 'Selecione pelo menos 2 arquivos PDF.',
                        'max_num': 'Selecione no máximo 50 arquivos PDF.',
                        'max_file_size': 'O tamanho do arquivo não pode exceder 100MB.'},
        validators=[validate_pdf],
    )

# =================================

class CustomMultiFileField(MultiFileField):
    def to_python(self, data):
        if not data:
            return None
        
        files = [file for file in data if file]
        return files

class SplitPDFForm(forms.Form):
    pdf_file = CustomMultiFileField(
        label='Selecione o arquivo PDF',
        min_num=1,
        validators=[validate_pdf]
    )