import React, { useState } from 'react';
import {
  View,
  Text,
  Button,
  ScrollView,
  StyleSheet
} from 'react-native';

export default function My_App_ContactosScreen({ navigation }) {
  const [Contacto, setContactos] = useState([
    { id: 1, title: 'Alberto Morales'},
    { id: 2, title: 'Juan Rojas'},
    { id: 3, title: 'Marcela Parias'},
  ]);
  const [filterMode, setFilterMode] = useState('all'); 

  const addContacto = (Contacto) => {
    setContactos (prev => [...prev, contacto]);
  };

  let displayedContacto;
  switch (filterMode) {
    case 'pending':
      displayedContacto = Contacto.filter(t => !t.completed);
      break;
    case 'completed':
      displayedContacto = Contacto.filter(t => t.completed);
      break;
    default:
      displayedContacto = Contacto;
  }

  return (
    <View style={styles.container}>
      <Text>Contacto Nuevo</Text>
      {/* Fila de botones de filtro */}
      <View style={styles.filterRow}>
        <Button
          title="Agregar Contacto"
          onPress={() => setFilterMode('all')}
          color={filterMode === 'all' ? '#007AFF' : undefined}
        />
        <Button
          title="Nombre"
          onPress={() => setFilterMode('pending')}
          color={filterMode === 'pending' ? '#007AFF' : undefined}
        />
        <Button
          title="Telefono"
          onPress={() => setFilterMode('completed')}
          color={filterMode === 'completed' ? '#007AFF' : undefined}
        />
      </View>

      {/* Lista filtrada */}
      <ScrollView style={styles.list}>
        {displayedContactos.map(Contacto=> (
          <View key={Contacto.id} style={styles.ContactoRow}>
            <Text style={styles.icon}>
              {Contacto.completed ? '✅' : '⌛️'}
            </Text>
            <Text
              style={[
                styles.ContactText,
                Contact.completed ? styles.completedText : styles.pendingText,
              ]}
            >
              {Contact.title}
            </Text>
          </View>
        ))}
      </ScrollView>

    
      <Button
        title="Crear Nuevo Contacto"
        onPress={() => navigation.navigate('AddContacto', { addContacto })}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container:    { flex: 1, padding: 16, backgroundColor: '#fff' },
  filterRow:    { flexDirection: 'row', justifyContent: 'space-around', marginBottom: 12 },
  list:         { flex: 1, marginBottom: 12 },
  ContactRow:      { flexDirection: 'row', alignItems: 'center', marginBottom: 8 },
  icon:         { fontSize: 18, marginRight: 8 },
  Contactoext:     { fontSize: 16 },
  
});