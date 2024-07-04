import subprocess
import tempfile
import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='Conversión de texto a voz con Edge TTS')
parser.add_argument('--voz', type=str, default='es-MX-JorgeNeural', help='Voz para la conversión')
args = parser.parse_args()

def read_text_from_file(file_path):
    """Lee el texto desde un archivo"""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().strip()
    return text

def convert_text_to_speech(text):
    global args
    """Convierte el texto en voz utilizando Edge TTS"""
    try:
        # Crear un archivo temporal para almacenar el audio
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio_file:
            output_file_path = temp_audio_file.name

        # Agregar comillas alrededor del texto
        quoted_text = f'"{text}"'
        # Ejecutar el comando edge-tts para convertir el texto en audio
        command = [
            "edge-tts",
            "--rate=+5%",
            "--voice",
            args.voz,
            "--text",
            quoted_text,
            "--write-media",
            output_file_path
        ]

        subprocess.run(command, capture_output=True)

        # Mover el archivo temporal a la ubicación deseada (salida.mp3)
        if os.path.exists(output_file_path):
            shutil.move(output_file_path, "salida.mp3")
            print("Conversión completada. El archivo de salida es 'salida.mp3'.")
        else:
            print("Error al generar el archivo de salida.")
    except Exception as e:
        print(f"Error durante la conversión: {e}")

if __name__ == "__main__":
    # Leer el texto desde el archivo de entrada
    input_file = "entrada.txt"
    text_to_speak = read_text_from_file(input_file)

    # Procesar el texto para convertirlo en audio
    convert_text_to_speech(text_to_speak)
