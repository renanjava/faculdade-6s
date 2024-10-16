import 'package:flutter/material.dart';
import 'screens/form.dart';
import 'model/transaction.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Aplicação Bancária',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Aplicação Bancária'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final List<Transaction> _transacoes = [];
  void _adicionarNovaTransacao() {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => TransactionForm(),
      ),
    ).then((result) {
      if (result != null && result is Transaction) {
        setState(() {
          _transacoes.add(result);
        });
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'Transações:',
            ),
            Expanded(
              child: ListView.builder(
                itemCount: _transacoes.length,
                itemBuilder: (context, index) {
                  final transacao = _transacoes[index];
                  return ListTile(
                    title: Text(transacao.name),
                    subtitle: Text('valor: ${transacao.values}'),
                    onTap: () {
                    },
                  );
                },
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _adicionarNovaTransacao,
        tooltip: 'Nova Transação',
        child: const Icon(Icons.add),
      ),
    );
  }
}