import React, { useState } from 'react';
import { View, Text, Button, TouchableOpacity, StyleSheet } from 'react-native';
import { useNavigation } from '@react-navigation/native';

export default function ContactListScreen() {
  const [contacts, setContacts] = useState([
    { nombre: 'Ana', telefono: '123456789', favorite: false },
    { nombre: 'Luis', telefono: '987654321', favorite: false },
  ]);
  const [filterMode, setFilterMode] = useState('all'); // 'all' or 'favorites'
  const navigation = useNavigation();

  const addContact = (newContact) => {
    setContacts([...contacts, { ...newContact, favorite: false }]);
  };

  const handleToggleFavorite = (index) => {
    setContacts((prev) =>
      prev.map((c, i) =>
        i === index ? { ...c, favorite: !c.favorite } : c
      )
    );
  };

  // Dynamic filtering
  const filteredContacts = contacts.filter((c) =>
    filterMode === 'all' ? true : c.favorite
  );

  return (
    <View style={{ flex: 1, padding: 20 }}>
      <Text style={{ fontSize: 24, marginBottom: 10 }}>Mis Contactos</Text>
      <View style={styles.filterContainer}>
        <Button
          title="Todos"
          onPress={() => setFilterMode('all')}
          color={filterMode === 'all' ? 'blue' : 'gray'}
        />
        <Button
          title="Favoritos"
          onPress={() => setFilterMode('favorites')}
          color={filterMode === 'favorites' ? 'blue' : 'gray'}
        />
      </View>
      <Button
        title="Agregar contacto"
        onPress={() => navigation.navigate('Agregar', { addContact })}
      />
      {filteredContacts.length === 0 ? (
        <Text style={styles.noContacts}>No hay contactos</Text>
      ) : (
        filteredContacts.map((c, index) => (
          <TouchableOpacity key={index} onPress={() => handleToggleFavorite(index)}>
            <Text style={[styles.contact, c.favorite && styles.favorite]}>
              {c.favorite ? '⭐ ' : '☆ '}
              {c.nombre}: {c.telefono}
            </Text>
          </TouchableOpacity>
        ))
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  filterContainer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginVertical: 10,
  },
  contact: {
    fontSize: 18,
    paddingVertical: 4,
  },
  favorite: {
    color: 'gold',
    fontWeight: 'bold',
  },
  noContacts: {
    marginTop: 20,
    fontStyle: 'italic',
    color: 'gray',
  },
});