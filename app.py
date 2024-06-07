from flask import Flask, render_template, request, redirect, url_for
from logger import setup_logger

app = Flask(__name__)
log = setup_logger("app")

# Initial list of tasks
tasks = []


@app.route('/')
def tasks():
    log.info('function tasks called')
    return render_template('index.html', tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    if task.strip():
        tasks.append(task.strip())
    return redirect(url_for('index'))


@app.route('/edit_task/<int:index>', methods=['POST'])
def edit_task(index):
    new_task = request.form['new_task']
    if new_task.strip():
        tasks[index] = new_task.strip()
    return redirect(url_for('index'))


@app.route('/delete_task/<int:index>')
def delete_task(index):
    log.info('function tasks called')
    del tasks[index]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
