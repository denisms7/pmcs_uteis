from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio


class ProgressViewConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send_progress()

    async def disconnect(self, close_code):
        # Lidar com a desconexão do cliente
        pass

    async def receive(self, text_data=None, bytes_data=None):
        # Lidar com as mensagens recebidas (opcional)
        pass

    async def send_progress(self):
        progress = 0
        while progress <= 100:
            await asyncio.sleep(1)  # Simula algum processo em andamento
            await self.send(text_data=f'Progresso: {progress}%')
            progress += 10
