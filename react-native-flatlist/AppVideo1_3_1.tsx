import { Text, TextInput, View } from 'react-native';
import { estilos } from './styles/estilos';
import Contato from './Contato';
import { useState } from 'react';

export default function AppVideo1_2_2() {

  const lista : Contato[] = [
    {id: 1, nome:"João Silva", telefone: "(11) 1111-1111", email: "joao@teste.com"},
    {id: 2, nome:"Maria Silva", telefone: "(11) 2222-2222", email: "maria@teste.com"},
    {id: 3, nome:"Jose Santos", telefone: "(11) 3333-3333", email: "jose@teste.com"},
    {id: 4, nome:"Marta Gonçalves", telefone: "(11) 4444-4444", email: "marta@teste.com"}
  ]

  const [filtroNome, setFiltroNome] = useState<string>("");

  const listaVisual = lista
                        .filter((item)=>item.nome.includes( filtroNome))
                        .map((item)=>
                              (<View style={estilos.secondaryContainer}>
                                <Text style={estilos.title}>{item.nome}</Text>
                                <Text>{item.telefone}</Text>
                                <Text>{item.email}</Text>
                              </View>))

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
