import 'dart:convert';

import 'package:http/http.dart' as http;

abstract class AbstractApi {
    final _urlLocalHost = 'http://localhost:3000';
    late String _resource;
    //const AbstractApi(this._resource);

    Future<String> getAll() async{
        var response = await http.get(Uri.parse('$_urlLocalHost/$_resource'));
        return response.body;
    }

    Future<String> getById(String id) async{
        var response = await http.get(Uri.parse('$_urlLocalHost/$_resource/$id'));
        return response.body;
    }

    Future<String> post() async{
      var response = await http.post(Uri.parse('$_urlLocalHost/$_resource'), 
      headers: <String, String>{
        'Content-type': 'application/json'
      },
      body: jsonEncode(<String, void>{
        'id': 5,
        'name': 'renan',
        'value': 600
      })
      );
      return response.body;
    }

    Future<String> patch() async{
      var response = await http.patch(Uri.parse('$_urlLocalHost/$_resource'), 
      headers: <String, String>{

      },
      body: jsonEncode(<String, void>{
        'id': 5,
        'name': 'renan',
        'value': 600
      })
      );
      return response.body;
    }

    Future<String> delete() async{
        var response = await http.delete(Uri.parse('$_urlLocalHost/$_resource'))
        return response.body;
    }
}