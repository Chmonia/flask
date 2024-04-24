from flask import Flask, url_for, render_template, request

app = Flask(__name__)

sp = ["Человечество вырастает из детства.", "Человечеству мала одна планета.", "Мы сделаем обитаемыми безжизненные "
      "пока планеты.", "И начнем с Марса!", "Присоединяйся!"]


@app.route('/')
def start():
    return f"Миссия Колонизация Марса"


@app.route('/index')
def index():
    return f"И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '</br>'.join(sp)


@app.route('/image_mars')
def mars_img():
    return f'''<!DOCTYPE html>
                 <html lang="en-US">
                   <head>
                     <meta charset="utf-8">
                     <meta name="viewport" content="width=device-width">
                     <title>Жди нас, Марс!</title>
                   </head>
                   <body>
                    <h1>Жди нас, Марс!</h1>
                    <figure>
                        <img src="{url_for('static', filename='img/Mars.jpg')}" 
                        alt="здесь должна была быть картинка, но не нашлась"
                        width=500px>
                        <figcaption>Вот она какая, красная планета.</figcaption>
                    </figure>
                   </body>
                 </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Загрузка фотографии</title>
                          </head>
                          <body>
                            <div class="card">
                                <h1>Загрузка фотографии</h1>
                                <h2>Для участия в миссии</h2>
                                <form method="post" enctype="multipart/form-data">
                                    <figure>
                                        <img src="{url_for('static', filename='data/im.png')}"
                                        alt="здесь должно быть выше фото))"
                                        width=500px>
                                    </figure>
                                    <div class="form-group">
                                        <label for="photo">Выберите файл</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        with open('static/data/im.png', "wb") as file:
            file.write(f.read())
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
