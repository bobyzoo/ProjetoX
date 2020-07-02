import tekore as tk


class Spotify(object):

    def __init__(self):
        self.client_id = '04b4767cc75549d7a19f70985c837dcb'
        self.client_secret = 'cfbd881c349a409ab4794b2547889ce1'
        self.redirect_uri = 'http://localhost/teste/spotifyTeste.php'
        self.cred = tk.Credentials(self.client_id, self.client_secret, self.redirect_uri)
        self.app_token = tk.request_client_token(self.client_id, self.client_secret)
        self.spotify = tk.Spotify(self.app_token)
        self.inicialize = False

    def inicialization(self):
        try:
            user_token = tk.prompt_for_user_token(
                self.client_id,
                self.client_secret,
                self.redirect_uri,
                scope=tk.scope.every
            )

            self.spotify.token = user_token
            return 'Inicializado com sucesso!'
        except:
            return 'Erro ao conectar com spotify'

    def check_inicialize(self):
        try:
            if not self.inicialize:
                self.inicialization()
            return True
        except:
            return False

    def pause(self):
        if self.check_inicialize():
            self.spotify.playback_pause()
            return 'Iniciando'
        else:
            return 'Erro'

    def resume(self):
        if self.check_inicialize():
            self.spotify.playback_resume()
            return 'Iniciando'
        else:
            return 'Erro'

    def player(self):
        if self.check_inicialize():
            self.spotify.playback_start_tracks(['2e7UGyxFACAfwHjmgNNMbS'])
            return 'Iniciando'
        else:
            return 'Erro'
