# João Pedro: Trail Quest

Corrida infinita de bicicleta inspirada no **chrome://dino**: João Pedro pedala sozinho por uma trilha que fica **mais rápida e mais difícil** quanto mais longe você chega. O objetivo é bater o recorde de distância.

## Como rodar

```bash
python3 -m pip install -r requirements.txt
python3 main.py
```

## Como rodar via web na porta 8085

Para servir no proprio servidor/local network:

```bash
rm -rf .venv build dist
./setup_web.sh
./serve_web.sh
```

O `setup_web.sh` cria um ambiente virtual fora da pasta do jogo, por padrao em `~/.venvs/joao_pedro_trail`, e instala as dependencias nele. Isso evita o erro `externally-managed-environment` em sistemas que bloqueiam instalacao global via `pip` e tambem evita que o pygbag tente empacotar uma `.venv` grande junto com o jogo.

No desktop o jogo abre em `1280x720`. No web ele usa `960x540` com `image-rendering: pixelated` para evitar que o navegador redimensione o canvas com borrado e deixe o texto ilegivel.

Depois acesse:

```text
http://localhost:8085
```

De outro dispositivo na mesma rede, use:

```text
http://IP_DO_SERVIDOR:8085
```

Se a pagina ficar parada em `Loading, please wait ... download`, force o host publico usado pelo pygbag:

```bash
hostname -I
tailscale ip -4
WEB_HOST=IP_DO_SERVIDOR ./serve_web.sh
```

Use um IP que apareca no `hostname -I` ou no `tailscale ip -4` rodado dentro do servidor remoto. O IP mostrado no log de acesso pode ser o IP do cliente/navegador, e nao deve ser usado no `WEB_HOST` se nao estiver configurado no servidor.

Se o ambiente virtual ficar com permissao quebrada, recrie-o:

```bash
rm -rf ~/.venvs/joao_pedro_trail
./setup_web.sh
```

Se o `rm -rf` falhar por permissao:

```bash
sudo chown -R "$USER:$USER" ~/.venvs/joao_pedro_trail
rm -rf ~/.venvs/joao_pedro_trail
./setup_web.sh
```

Evite usar `0.0.0.0` como URL no navegador. O script tenta detectar o IP real com `hostname -I`; se ele escolher o IP errado, use `WEB_HOST`.

Para gerar somente os arquivos estaticos:

```bash
python3 -m pygbag --build .
```

O build web fica em `build/web/`.

> No macOS, se a instalação do Pygame falhar por erros de SDL, rode:
>
> ```bash
> brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf pkg-config
> ```

## Controles

- A bicicleta anda sozinha.
- **Espaço / W / seta para cima**: pular (segure para pular mais alto, solte para um pulo curto)
- **Baixo / S**: agachar (única forma de passar por baixo dos pássaros)
- **M**: ligar/desligar a música
- **R**: reiniciar depois de perder
- **ESC**: sair (o recorde é salvo)

## Como funciona (estilo dino)

- **Velocidade crescente**: começa em 2.4 e sobe continuamente até o teto de 4.6 por volta dos ~700m. O velocímetro no HUD mostra a aceleração em tempo real.
- **Dificuldade crescente**: a cada nível (250m) a janela de reação entre obstáculos encolhe (de ~52 para ~24 frames). Surgem variações conforme avança:
  - **Pedras altas** (nível 1+): exigem um pulo mais completo, não dá para passar com um pulinho.
  - **Grupos de pedras** (duplas no nível 2+, triplas no nível 5+): limpáveis num pulo só, mas com timing apertado.
  - **4º obstáculo por trecho** (nível 4+): trilha mais cheia.
  - **Pássaros** (a partir de ~900m): voam baixo e **só são evitados agachando**.
- **Baús bem mais raros**: agora são probabilísticos, espaçados em pelo menos 6 trechos (~190m), ficam mais raros com a distância e só dão vida quando você não está no máximo — o jogo não é mais "fácil de mais" por causa deles.
- **Pulo com sensação melhor**: altura variável, "flutuada" no ápice, *coyote time* e *buffer* de pulo perdoam pequenos erros de tempo nas velocidades altas.
- **Combo**: passar por obstáculos sem bater acumula um combo que vale pontos crescentes — bateu, zera.
- **Feedback**: poeira ao pousar, tremor de tela + flash vermelho ao tomar dano, popups de pontos e de "LEVEL UP".
- **Cenário**: background com mais camadas de parallax, sol, colinas, cercas, arbustos, flores e pedras.

## Itens

- **Moedas**: +1 ponto.
- **Estrelas**: +5 pontos.
- **Cogumelo**: boost de velocidade temporário, sem efeito visual extra.
- **Baú / mamadeira**: recupera 1 vida (até 5 corações).

## Áudio

Música 8-bit gerada pelo próprio jogo (sem arquivo externo), reescrita para cansar menos: melodia mais longa (loop de ~10s em lá-menor pentatônica, com frases A/B), timbre mais suave (mistura de triângulo + pulso com envelope ADSR e um leve filtro passa-baixa), batida grave discreta só nos tempos fortes e volume mais baixo. Os efeitos sonoros seguem o mesmo timbre suave.

## Testes

```bash
SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy python3 smoke_test.py    # valida física, fairness e o loop completo, sem janela
SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy python3 render_frames.py # gera PNGs dos frames em /tmp/trailquest para conferência visual
```

Desenvolvido por **@rafaelcotote**.
