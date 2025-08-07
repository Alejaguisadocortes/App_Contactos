import React, { useState } from 'react';
import {
  View,
  Text,
  Button,
  ScrollView,
  StyleSheet,
  TouchableOpacity,
} from 'react-native';

export default function My_App_ContactosScreen({ navigation }) {
  const [contactos, setContactos] = useState([
    { id: 1, title: 'Alberto Morales' },
    { id: 2, title: 'Juan Rojas' },
    { id: 3, title: 'Marcela Parias' },
  ]);

  const [filterMode, setFilterMode] = useState('all');

  const addContacto = (nuevoContacto) => {
    setContactos((prev) => [...prev, nuevoContacto]);
  };

  // Filtro simple (por ahora muestra todos, puedes agregar favoritos después)
  const displayedContactos = contactos; // puedes cambiar esto según el filtro

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Mis Contactos</Text>

      {/* Fila de botones de filtro */}
      <View style={styles.filterRow}>
        <Button
          title="Todos"
          onPress={() => setFilterMode('all')}
          color={filterMode === 'all' ? '#007AFF' : undefined}
        />
        <Button
          title="Nombre"
          onPress={() => setFilterMode('nombre')}
          color={filterMode === 'nombre' ? '#007AFF' : undefined}
        />
        <Button
          title="Teléfono"
          onPress={() => setFilterMode('telefono')}
          color={filterMode === 'telefono' ? '#007AFF' : undefined}
        />
      </View>

      {/* Lista filtrada */}
      <ScrollView style={styles.list}>
        {displayedContactos.map((contacto) => (
          <View key={contacto.id} style={styles.contactRow}>
            <Text style={styles.icon}>📇</Text>
            <Text style={styles.contactText}>{contacto.title}</Text>
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
  container: { flex: 1, padding: 16, backgroundColor: '#fff' },
  header: { fontSize: 24, marginBottom: 12 },
  filterRow: { flexDirection: 'row', justifyContent: 'space-around', marginBottom: 12 },
  list: { flex: 1, marginBottom: 12 },
  contactRow: { flexDirection: 'row', alignItems: 'center', marginBottom: 8 },
  icon: { fontSize: 18, marginRight: 8 },
  contactText: { fontSize: 16 },
});
