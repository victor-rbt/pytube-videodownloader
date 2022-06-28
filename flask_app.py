from flask import Flask, request, send_file
from pytube import YouTube


app = Flask(__name__)

@app.route('/')
def test():
    return 'Its works!'


@app.route('/download')
def download():
    """."""
    url = request.args.get('url')
    if not url:
        return 'Você deve informar a url do vídeo!'

    yt = criar_instancia(url)
    video = yt.streams.filter(
        progressive=True, file_extension='mp4').first()
    return send_file(video.download(), as_attachment=True)

def criar_instancia(url):
    """."""
    return YouTube(url)

app.run(debug=True)