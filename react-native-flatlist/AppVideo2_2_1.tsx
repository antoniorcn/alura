import { Button, ScrollView, Text, TextInput, View } from 'react-native';
import { estilos } from './styles/estilos';
import Contato from './Contato';
import { useState } from 'react';
import ContatoDetalhe from './ClienteDetalhe';



export default function AppVideo1_2_2() {

  const [lista, setLista] = useState<Array<Contato>> ([
    {id: 1, nome:"João Silva", telefone: "1111-1111", email: "joao@teste.com"},
    {id: 2, nome:"Maria Silva", telefone: "2222-2222", email: "maria@teste.com"},
    {id: 3, nome:"Jose Santos", telefone: "3333-3333", email: "jose@teste.com"},
    {id: 4, nome:"Marta Gonçalves", telefone: "4444-4444", email: "marta@teste.com"},
    {id: 5, nome:"João Silva", telefone: "1111-1111", email: "joao@teste.com"},
    {id: 6, nome:"Maria Silva", telefone: "2222-2222", email: "maria@teste.com"},
    {id: 7, nome:"Jose Santos", telefone: "3333-3333", email: "jose@teste.com"},
    {id: 8, nome:"Marta Gonçalves", telefone: "4444-4444", email: "marta@teste.com"},
    {id: 9, nome:"João Silva", telefone: "1111-1111", email: "joao@teste.com"},
    {id: 10, nome:"Maria Silva", telefone: "2222-2222", email: "maria@teste.com"},
    {id: 11, nome:"Jose Santos", telefone: "3333-3333", email: "jose@teste.com"},
    {id: 12, nome:"Marta Gonçalves", telefone: "4444-4444", email: "marta@teste.com"}
  ]);

  const [filtroNome, setFiltroNome] = useState<string>("");

  const listaVisual = lista
                        .filter((item : Contato)=>item.nome.includes( filtroNome))
                        .map((item : Contato, idx : number)=>
                              <ContatoDetalhe contato = {item}/>)

  return(
    <View style={estilos.container}>
      <View style={{flex: 1, flexDirection:"row", justifyContent: "space-between"}}>
        <Text style={{flex: 1, marginVertical: 20}}>Filtro:</Text>
        <TextInput style={[{flex: 3, marginVertical: 20}, estilos.textInput]} 
        value={filtroNome} onChangeText={setFiltroNome}/>
        <Button title="Inserir" onPress={()=>{
            setLista( [...lista, 
              {id: 13, nome:"Maria Silva", telefone: "2222-2222", email: "maria@teste.com"}]);
            }} />
      </View>
      <View style={{flex: 8}}>
        <ScrollView horizontal={false}>
          {listaVisual}
        </ScrollView>
      </View>
    </View>
  )
}
