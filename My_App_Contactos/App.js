const express = require('express');
const app = express();
const path = require('path');

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.get('/', (req, res) => {
    const titulo = "Mis Contactos App"; 
       res.render('index', { titulo: titulo }); 
});

import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

const appTitle = "Lista de Contactos";
const contacts = [
  { id: 1, name: "Santiago Parra", phone: "3004223154", favorite: false },
  { id: 2, name: "Juan Emilio Pasos", phone: "3207776834", favorite: true },
  { id: 3, name: "Marcela Juarez", phone: "3154329065", favorite: false },
  { id: 4, name: "Pedro Pablo Jaramillo", phone: "3014395438", favorite: true },
  { id: 5, name: "Heladio Heredia", phone: "3234782314", favorite: true },
  { id: 6, name: "Pilicra Potes", phone: "3508743322", favorite: true },
];

const App = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{appTitle}</Text>
      {contacts.map((contact) => (
        <View key={contact.id}>
          <Text>{contact.name}</Text>
          <Text>{contact.phone}</Text>
        </View>
      ))}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
  },
  title: {
    fontSize: 23,
    fontWeight: 'bold',
    marginBottom: 20,
  },
});

export default App;