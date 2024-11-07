import amqp from 'amqplib';

async function sendTasks() {

    try{
        const connection = await amqp.connect('amqp://localhost');
        const channel = await connection.createChannel();
    
        const queue = 'task_queue';
        const msg = process.argv.slice(2).join(' ') || 'Tarefa padrão';
    
        await channel.assertQueue(queue, {
            durable: true
        })
    
        channel.sendToQueue(queue, Buffer.from(msg), {
            persistent: true
        });
    
        console.log(" [x] Enviando '%s'", msg);
    
        setTimeout(() => {
            connection.close()
            process.exit(0)
        }, 500);
        
    }catch(err){
        console.error(err);
    }

}

sendTasks()