import { View, Text, Button } from 'react-native';

export default function ContactListScreen({ navigation, contacts, addContact }) {
  return (
    <View>
      <Text>Lista de Contactos</Text>
      <Button
        title="Agregar Contacto"
        onPress={() => navigation.navigate('AddContact', { addContact })}
      />
        </View>
      );
    }