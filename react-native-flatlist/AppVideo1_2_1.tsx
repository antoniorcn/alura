import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { estilos } from './styles/estilos';
import Contato from './Contato';

export default function AppVideo1_2_1() {

  const lista : Contato[] = [
    {id: 1, nome:"João Silva", telefone: "(11) 1111-1111", email: "joao@teste.com"},
    {id: 2, nome:"Maria Silva", telefone: "(11) 2222-2222", email: "maria@teste.com"},
    {id: 3, nome:"Jose Santos", telefone: "(11) 3333-3333", email: "jose@teste.com"},
    {id: 4, nome:"Marta Gonçalves", telefone: "(11) 4444-4444", email: "marta@teste.com"}
  ]

  return (
    [
      <View style={estilos.secondaryContainer}>
        <Text style={estilos.title}>João Silva</Text>
        <Text>Tel.: (11) 1111-1111</Text>
        <Text>joao@teste.com</Text>
      </View>,
      <View style={estilos.secondaryContainer}>
        <Text style={estilos.title}>Maria Silva</Text>
        <Text>Tel.: (11) 2222-2222</Text>
        <Text>maria@teste.com</Text>
      </View>,
      <View style={estilos.secondaryContainer}>
        <Text style={estilos.title}>Jose Santos</Text>
        <Text>Tel.: (11) 3333-3333</Text>
        <Text>jose@teste.com</Text>
      </View>, 
      <View style={estilos.secondaryContainer}>
        <Text style={estilos.title}>Marta Gonçalves</Text>
        <Text>Tel.: (11) 4444-4444</Text>
        <Text>marta@teste.com</Text>
      </View>            
    ]
  );
}
