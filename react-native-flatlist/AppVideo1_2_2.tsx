import { Text, View } from 'react-native';
import { estilos } from './styles/estilos';
import Contato from './Contato';

export default function AppVideo1_2_2() {

  const lista : Contato[] = [
    {id: 1, nome:"João Silva", telefone: "1111-1111", email: "joao@teste.com"},
    {id: 2, nome:"Maria Silva", telefone: "2222-2222", email: "maria@teste.com"},
    {id: 3, nome:"Jose Santos", telefone: "3333-3333", email: "jose@teste.com"},
    {id: 4, nome:"Marta Gonçalves", telefone: "4444-4444", email: "marta@teste.com"}
  ]

  const listaVisual = []
  for (let i = 0; i < lista.length; i++) { 
    listaVisual.push(
      <View style={estilos.secondaryContainer}>
        <Text style={estilos.title}>{lista[i].nome}</Text>
        <Text>{lista[i].telefone}</Text>
        <Text>{lista[i].email}</Text>
      </View>
    )
  }

  return listaVisual;
}
