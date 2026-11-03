# João Pedro: Trail Quest

Corrida infinita de bicicleta inspirada no **chrome://dino**: João Pedro pedala sozinho por uma trilha que fica mais rápida e mais difícil quanto mais longe você chega. O objetivo é bater o recorde de distância.

## Como jogar

Abra `index.html` no navegador. Para celular ou outro computador, sirva a pasta e compartilhe o endereço:

```bash
python3 -m http.server 8085
```

Depois acesse `http://localhost:8085`. Em outro aparelho na mesma rede, use `http://IP_DO_COMPUTADOR:8085`.

O recorde fica salvo no navegador.

## Como rodar via Docker Compose

```bash
docker compose up --build
```

Depois acesse `http://localhost:8085`. O container serve a página do jogo.

## Controles

- A bicicleta anda sozinha.
- **Toque, espaço, W ou seta para cima**: pular. Segurar faz o pulo ir mais alto.
- **Seta para baixo ou S**: agachar, para passar por baixo dos pássaros e dos galhos.
- No celular, os botões **Pular** e **Agachar** aparecem embaixo da tela.
- **M**: ligar ou desligar a música.
- **Toque ou R**: reiniciar depois de perder.

## O jogo

- João Pedro pedala automaticamente. O jogador controla o pulo e o agachar.
- A velocidade sobe com a distância e tem um teto.
- Moedas, estrelas, cogumelos e baús mudam a pontuação, a vida e a velocidade.
- A partir de cerca de 140 m aparecem pássaros e galhos baixos. O agachar passa por baixo. O galho é comprido demais para um pulo.
- O recorde de distância aparece no painel da trilha.
