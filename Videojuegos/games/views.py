import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import games
from .forms import GamesForm, RequerimientosFrom


# Create your views here.
def lista_juegos(request):
    juegos = games.objects.select_related('requerimientos_sistema').all()
    return render(request, 'juegos/lista_juegos.html', {'juegos': juegos})

def detalle_juego(request, id):
    juego = get_object_or_404(games.objects.select_related('requerimientos_sistema'), id=id)
    return render(request, 'juegos/detalle_juego.html', {'juego': juego})

def crear_juego(request):
    juego_data = None
    game_form = GamesForm()
    req_form = RequerimientosFrom()

    if 'buscar' in request.GET:
        titulo_buscado = request.GET.get('buscar')
        api_url = "https://www.freetogame.com/api/games"

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            juego_api = next((j for j in data if titulo_buscado.lower() in j['title'].lower()), None)

            if juego_api:
                detalle_url = f"https://www.freetogame.com/api/game?id={juego_api['id']}"
                detalle_response = requests.get(detalle_url)
                detalle_response.raise_for_status()
                detalle_data = detalle_response.json()
                game_form = GamesForm(initial={
                    'titulo': detalle_data.get('title'),
                    'estado': detalle_data.get('status'),
                    'imagen': detalle_data.get('thumbnail'),
                    'descripcion_pequeña': detalle_data.get('short_description'),
                    'descricpcion': detalle_data.get('description')[:100],
                    'genero': detalle_data.get('genre'),
                    'editor': detalle_data.get('publisher'),
                    'fecha': detalle_data.get('release_date'),
                    'game_url': detalle_data.get('game_url'),
                })

                requisitos = detalle_data.get('minimum_system_requirements', {})
                req_form = RequerimientosFrom(initial={
                    'sistema': requisitos.get('os'),
                    'procesador': requisitos.get('processor'),
                    'memoria': requisitos.get('memory'),
                    'grafica': requisitos.get('graphics'),
                    'almacenamiento': requisitos.get('storage'),
                })
                juego_data = detalle_data
        except requests.exceptions.RequestException as e:
            print(f"Error al buscar el juego: {e}")

    if request.method == 'POST':
        game_form = GamesForm(request.POST)
        req_form = RequerimientosFrom(request.POST)

        if game_form.is_valid() and req_form.is_valid():
            requisitos = req_form.save()
            juego = game_form.save(commit=False)
            juego.requerimientos_sistema = requisitos
            juego.save()
            return redirect('lista_juegos')

    return render(request, 'juegos/form_juego.html', {
        'game_form': game_form,
        'req_form': req_form,
        'juego_data': juego_data
    })


def editar_juego(request, id):
    juego = get_object_or_404(games, id=id)

    if request.method == 'POST':
        form = GamesForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('detalle_juego', id=juego.id)
    else:
        form = GamesForm(instance=juego)

    return render(request, 'juegos/editar_juego.html', {'form': form, 'juego': juego})


def eliminar_juego(request, id):
    juego = get_object_or_404(games, id=id)

    if request.method == 'POST':
        juego.delete()
        return redirect('lista_juegos')

    return render(request, 'juegos/confirmar_eliminacion.html', {'juego': juego})