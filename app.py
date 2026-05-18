from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'vortextech'


# =========================
# LOGIN
# =========================
@app.route('/')
def login():
    return render_template('login.html')


# =========================
# CADASTRO
# =========================
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


# =========================
# LOGAR
# =========================
@app.route('/logar', methods=['POST'])
def logar():

    usuario_fake = {
        'id_usuario': 1,
        'nome': 'Usuário'
    }

    session['usuario'] = usuario_fake

    return redirect('/dashboard')


# =========================
# CADASTRAR
# =========================
@app.route('/cadastrar', methods=['POST'])
def cadastrar():

    return redirect('/')


# =========================
# DASHBOARD
# =========================
@app.route('/dashboard')
def dashboard():

    if 'usuario' not in session:
        return redirect('/')

    return render_template(
        'index.html',
        usuario=session['usuario']
    )


# =========================
# PERFIL
# =========================
@app.route('/perfil')
def perfil():

    if 'usuario' not in session:
        return redirect('/')

    return render_template(
        'perfil.html',
        usuario=session['usuario'],
        perfil=None
    )


# =========================
# ATUALIZAR PERFIL
# =========================
@app.route('/atualizar_perfil', methods=['POST'])
def atualizar_perfil():

    return redirect('/perfil')


# =========================
# ENEM
# =========================
@app.route('/enem')
def enem():

    if 'usuario' not in session:
        return redirect('/')

    return render_template('enem.html')


# =========================
# VESTIBULARES
# =========================
@app.route('/vestibulares')
def vestibulares():

    if 'usuario' not in session:
        return redirect('/')

    return render_template('vestibulares.html')


# =========================
# VAGAS
# =========================
@app.route('/vagas')
def vagas():

    if 'usuario' not in session:
        return redirect('/')

    return render_template('vagas.html')


# =========================
# CONCURSOS
# =========================
@app.route('/concursos')
def concursos():

    if 'usuario' not in session:
        return redirect('/')

    return render_template('concursos.html')


# =========================
# DICAS DE EMPREGO
# =========================
@app.route('/dicas')
def dicas():

    if 'usuario' not in session:
        return redirect('/')

    return render_template('dicasdeemprego.html')


# =========================
# PROGRAMAS
# =========================
@app.route('/programas')
def programas():

    if 'usuario' not in session:
        return redirect('/')

    return render_template('programas.html')


# =========================
# LOGOUT
# =========================
@app.route('/logout')
def logout():

    session.clear()

    return redirect('/')


# =========================
# INICIAR SERVIDOR
# =========================
app.run(host='0.0.0.0', port=10000)
