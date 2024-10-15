class Transaction {
  final int id;
  final String name;
  final double values;

  Transaction({required this.id, required this.name, required this.values});

  factory Transaction.fromJson(Map<String, dynamic> json) {
    return Transaction(
      id: json['id'],
      name: json['name'],
      values: json['values'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'values': values,
    };
  }
}