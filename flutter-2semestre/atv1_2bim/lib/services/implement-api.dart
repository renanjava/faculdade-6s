import 'dart:convert';
import 'dart:core';

import 'package:atv1_2bim/services/abstract-api.dart';
import 'package:atv1_2bim/services/transaction.dart';
import 'package:http/http.dart' as http;


class ImplementApi extends AbstractApi<Transaction> {
    final _urlLocalHost = 'http://localhost:3000';
    var create = jsonEncode(<String, dynamic>{
        'id': 1,
        'name': 'renan',
        'value': 600
      });

    @override
      Future<List<Transaction>> getAll() async{
        var response = await http.get(Uri.parse(_urlLocalHost));
        return response.body;
    }

    @override
      Future<Transaction> getById(String id) async{
        var response = await http.get(Uri.parse(_urlLocalHost));
        return response.body;
    }

    @override
      Future<Transaction> post(String id) async{
      var response = await http.post(Uri.parse(_urlLocalHost), 
      headers: <String, String>{
        'Content-type': 'application/json'
      },
      body: jsonEncode(<String, dynamic>{
        'id': 1,
        'name': 'renan',
        'value': 600
      })
      );
      return response.body;
    }

    @override
      Future<Transaction> patch(String id) async{
      var response = await http.patch(Uri.parse(_urlLocalHost), 
      headers: <String, String>{

      },
      body: jsonEncode(<String, dynamic>{
        'id': 1,
        'name': 'renan2',
        'value': 600
      })
      );
      return response.body;
    }

    @override
      Future<void> delete(String id) async{
        await http.delete(Uri.parse(_urlLocalHost));
    }
}