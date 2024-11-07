import amqp from 'amqplib'

async function receiveTasks(){
    try{
        const connection = await amqp.connect('amqp://localhost');
        const channel = await connection.createChannel();
        
        const queue = 'task_queue';
    
        await channel.assertQueue(queue, {
            durable: true
        })
        
        channel.prefetch(1)
        console.log(" [*] Aguardando mensagens. Para sair, pressione CTRL+C");
        channel.consume(queue, (msg) => {
            const secs = msg.content.toString().split('.')
            console.log(" [X] Recebido '%s'", msg.content.toString());
    
            setTimeout(() => {
                console.log(" [X] Processado '%s'", msg.content.toString())
                channel.ack(msg)
            }, secs * 1000);
        }, {
            noAck: false
        })
    }catch(err){
        console.error(err);
    }
}

receiveTasks()