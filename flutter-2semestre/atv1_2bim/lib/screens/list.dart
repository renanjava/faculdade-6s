import 'package:atv1_2bim/model/transaction.dart';
import 'package:atv1_2bim/services/abstract_service.dart';
import 'package:flutter/material.dart';

class ListaTransacoes extends StatelessWidget {
  final ImplementService service;

  ListaTransacoes({required this.service});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Transações'),
      ),
      body: FutureBuilder<List<dynamic>>(
        future: service.getAll(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          }
          if (snapshot.hasError) {
            return Center(child: Text('Erro ao carregar transações'));
          }
          final transacoes = snapshot.data ?? [];
          return ListView.builder(
            itemCount: transacoes.length,
            itemBuilder: (context, index) {
              final transacao = transacoes[index];
              return ListTile(
                title: Text(transacao.name),
                subtitle: Text('R\$ ${transacao.values.toStringAsFixed(2)}'),
                trailing: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    IconButton(
                      icon: Icon(Icons.edit),
                      onPressed: () {
                      },
                    ),
                    IconButton(
                      icon: Icon(Icons.delete),
                      onPressed: () {
                        service.delete(transacao.id);
                      },
                    ),
                  ],
                ),
              );
            },
          );
        },
      ),
    );
  }
}
