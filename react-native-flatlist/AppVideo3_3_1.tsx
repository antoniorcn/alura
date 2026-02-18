import { Button, FlatList, ListRenderItemInfo, ScrollView, Text, TextInput, View } from 'react-native';
import { estilos } from './styles/estilos';
import Contato from './Contato';
import { useEffect, useState } from 'react';
import { FontAwesome as Icon} from '@expo/vector-icons';

interface ContatoDetalhesProps extends ListRenderItemInfo<Contato> { 
  onEditar( contato : Contato ) : void; 
  onApagar( id : number ) : void;
}

const ContatoDetalhe : React.FC<ContatoDetalhesProps>= ( props ) => {
  const item = props.item;
  return (
    <View key={"item-"+ item.id} style={[estilos.secondaryContainer, {flexDirection: "row", justifyContent: "space-between"}]}>
      <View style={{flex: 4}}>
        <Text style={estilos.title}>{item.nome}</Text>
        <Text>{item.telefone}</Text>
        <Text>{item.email}</Text>
      </View>
      <View style={{flex: 1, flexDirection: "row", justifyContent: "space-around"}}>
        <Icon name="edit" size={32} color="black" onPress={()=>props.onEditar( item )}/>
        <Icon name="trash" size={32} color="black" onPress={()=>props.onApagar( item.id )}/>
      </View>
    </View>
  )
}

export default function AppVideo3_3_1() {

  const contatos : Contato[] = [
    {id: 1, nome:"João Silva", telefone: "1111-1111", email: "joao@teste.com"},
    {id: 2, nome:"Maria Silva", telefone: "2222-2222", email: "maria@teste.com"},
    {id: 3, nome:"Jose Santos", telefone: "3333-3333", email: "jose@teste.com"},
    {id: 4, nome:"Marta Gonçalves", telefone: "4444-4444", email: "marta@teste.com"}
  ];

  const [lista, setLista] = useState<Contato[]>([]);

  useEffect( 
    ()=>{
      const listaTemp = [];
      for ( let i = 0; i < 2000; i++) { 
        const contato = contatos[ i % 4 ];
        listaTemp.push( { ...contato, id: i, nome: `${contato.nome} - ${i}` } );
      }
      setLista( listaTemp );
      console.log(`Lista Criada com ${listaTemp.length} elementos`);
    }, []
  );

  return (
    <FlatList   data={lista}
                initialNumToRender={10}
                maxToRenderPerBatch={10}
                windowSize={21}
                removeClippedSubviews={false}
                renderItem={flatProps =><ContatoDetalhe {...flatProps} 
                                                        onEditar={()=>{}} 
                                                        onApagar={()=>{}}/>}
                keyExtractor={ item => `contato-${item.id}`}
    />
  );
}
