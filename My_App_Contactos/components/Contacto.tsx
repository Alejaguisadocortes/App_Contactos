import { View, Text, StyleSheet } from 'react-native';

export default function Contacto({ nombre, telefono }: { nombre: string; telefono: string }) {
  return (
    <View style={styles.container}>
      <Text style={styles.nombre}>{nombre}</Text>
      <Text style={styles.telefono}>{telefono}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 12,
    backgroundColor: '#e0f7fa',
    borderRadius: 10,
    marginBottom: 10,
  },
  nombre: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  telefono: {
    fontSize: 16,
    color: '#555',
  },
});
