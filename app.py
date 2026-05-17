from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)

app.secret_key = 'vortextech'

# CONEXÃO MYSQL
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='vortex_tech'
)

cursor = conexao.cursor(dictionary=True)

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

    email = request.form['email']
    senha = request.form['senha']

    sql = '''
    SELECT * FROM usuarios
    WHERE email = %s
    AND senha = %s
    '''

    cursor.execute(sql, (email, senha))

    usuario = cursor.fetchone()

    if usuario:

        session['usuario'] = usuario

        return redirect('/dashboard')

    return 'Email ou senha inválidos'


# =========================
# CADASTRAR
# =========================
@app.route('/cadastrar', methods=['POST'])
def cadastrar():

    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    sql_verifica = '''
    SELECT * FROM usuarios
    WHERE email = %s
    '''

    cursor.execute(sql_verifica, (email,))

    usuario_existente = cursor.fetchone()

    if usuario_existente:
        return 'Este email já está cadastrado'

    sql = '''
    INSERT INTO usuarios
    (nome, email, senha)
    VALUES (%s, %s, %s)
    '''

    valores = (
        nome,
        email,
        senha
    )

    cursor.execute(sql, valores)

    conexao.commit()

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

    id_usuario = session['usuario']['id_usuario']

    sql = '''
    SELECT * FROM perfis
    WHERE id_usuario = %s
    '''

    cursor.execute(sql, (id_usuario,))

    perfil = cursor.fetchone()

    return render_template(
        'perfil.html',
        usuario=session['usuario'],
        perfil=perfil
    )


# =========================
# ATUALIZAR PERFIL
# =========================
@app.route('/atualizar_perfil', methods=['POST'])
def atualizar_perfil():

    if 'usuario' not in session:
        return redirect('/')

    idade = request.form['idade']
    cidade = request.form['cidade']
    interesse = request.form['interesse']

    id_usuario = session['usuario']['id_usuario']

    sql_verifica = '''
    SELECT * FROM perfis
    WHERE id_usuario = %s
    '''

    cursor.execute(sql_verifica, (id_usuario,))

    perfil_existente = cursor.fetchone()

    if perfil_existente:

        sql = '''
        UPDATE perfis
        SET idade = %s,
            cidade = %s,
            interesse = %s
        WHERE id_usuario = %s
        '''

        valores = (
            idade,
            cidade,
            interesse,
            id_usuario
        )

    else:

        sql = '''
        INSERT INTO perfis
        (idade, cidade, interesse, id_usuario)
        VALUES (%s, %s, %s, %s)
        '''

        valores = (
            idade,
            cidade,
            interesse,
            id_usuario
        )

    cursor.execute(sql, valores)

    conexao.commit()

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
app.run(debug=True)