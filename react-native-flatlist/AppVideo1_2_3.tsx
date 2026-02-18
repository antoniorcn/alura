import { Text, TextInput, View } from 'react-native';
import { estilos } from './styles/estilos';
import Contato from './Contato';
import { useState } from 'react';

export default function AppVideo1_2_2() {

  const lista : Contato[] = [
    {id: 1, nome:"João Silva", telefone: "1111-1111", email: "joao@teste.com"},
    {id: 2, nome:"Maria Silva", telefone: "2222-2222", email: "maria@teste.com"},
    {id: 3, nome:"Jose Santos", telefone: "3333-3333", email: "jose@teste.com"},
    {id: 4, nome:"Marta Gonçalves", telefone: "4444-4444", email: "marta@teste.com"}
  ]

  const [filtroNome, setFiltroNome] = useState<string>("");

  const listaVisual = [];
  for (let i = 0; i < lista.length; i++) { 
    const item = lista[i]
    if (item.nome.includes( filtroNome)) {
      listaVisual.push(
        <View style={estilos.secondaryContainer}>
          <Text style={estilos.title}>{lista[i].nome}</Text>
          <Text>{lista[i].telefone}</Text>
          <Text>{lista[i].email}</Text>
        </View>
      )
    }
  }

  return(
    <View style={estilos.container}>
      <View style={{flex: 1, flexDirection:"row", justifyContent: "space-between"}}>
        <Text style={{flex: 1, marginVertical: 20}}>Filtro:</Text>
        <TextInput style={[{flex: 3, marginVertical: 20}, estilos.textInput]} 
        value={filtroNome} onChangeText={setFiltroNome}/>
      </View>
      <View style={{flex: 8}}>
        {listaVisual}
      </View>
    </View>
  )
}
