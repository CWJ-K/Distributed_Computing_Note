import celery

app = celery.Celery(
    'test',
    broker='amqp://test:test@rabbitmq',
    backend='redis://redis' 
    )

@app.task
def echo(message):
    return message