from app import app


@app.route('/')
def index():
    return '<div> <P> É água pra todo lado,<br>  É muito sapo a coaxar,<br>  Vegetação vestindo verde,<br>  É o inverno a chegar.<br>  É a esperança brotando,<br>  No chão do meu Ceará.<br>  </P> </div>'
