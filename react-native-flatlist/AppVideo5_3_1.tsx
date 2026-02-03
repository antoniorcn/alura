import { Button, FlatList, ListRenderItemInfo, ScrollView, Text, TextInput, View } from 'react-native';
import { estilos } from './styles/estilos';
import Contato from './Contato';
import { useEffect, useRef, useState } from 'react';
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
        <Text style={estilos.title}>{`${item.nome} - ${item.id}`}</Text>
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
const ListaHeader = () => (
  <View style={{flex: 1, justifyContent: "center"}}>
    <Text style={estilos.headerText}>Inicio</Text>
  </View>
);

const ListaFooter = () => (
  <View style={{flex: 1, justifyContent: "center"}}>
    <Text style={estilos.headerText}>Termino</Text>
  </View>
);

const ItemSeparator = () => (
  <View style={estilos.flatListSeparator}/>
);

const EmptyList = () => (
  <View style={[estilos.flatListContainer, {alignItems: "center"}]}>
    <Text style={estilos.headerText}>Não há elementos na lista</Text>
  </View>
);


export default function AppVideo5_3_1() {

  const contatos : Contato[] = [
    {id: 1, nome:"João Silva", telefone: "(11) 1111-1111", email: "joao@teste.com"},
    {id: 2, nome:"Maria Silva", telefone: "(11) 2222-2222", email: "maria@teste.com"},
    {id: 3, nome:"Jose Santos", telefone: "(11) 3333-3333", email: "jose@teste.com"},
    {id: 4, nome:"Marta Gonçalves", telefone: "(11) 4444-4444", email: "marta@teste.com"}
  ];

  const [lista, setLista] = useState<Contato[]>([]);
  const flatListRef = useRef( null );

  useEffect( 
    ()=>{
      const listaTemp = [];
      for ( let i = 0; i < 100; i++) { 
        const contato = contatos[ i % 4 ];
        listaTemp.push( { ...contato, id: i } );
      }
      setLista( listaTemp );
      console.log(`Lista Criada com ${listaTemp.length} elementos`);
    }, []
  );

  return (
    <View style={{flex: 1}}>
      <View style={{flex: 1}}>
        <Text>Controles</Text>
        <Button title="Ir para o indice 50" onPress={()=>{
          flatListRef.current.scrollToIndex( {
            index: 50,
            animated: true,
            viewPosition: 1.0 // 0=topo, 0.5=meio, 1=fundo
          } );
        }} />
        <Button title="Voltar ao inicio da lista" onPress={()=>{
          flatListRef.current.scrollToOffset( {
            offset: 0, 
            animated: true,
          } );
        }} />
      </View>
      <View style={{flex: 4}}>
        <FlatList  ref={flatListRef}
              style={{flex: 1}}
              data={lista}
              ListHeaderComponent={ListaHeader}
              ListFooterComponent={ListaFooter}
              ListEmptyComponent={EmptyList}
              renderItem={flatProps =><ContatoDetalhe {...flatProps} 
                                                      onEditar={()=>{}} 
                                                      onApagar={()=>{}}/>}
              keyExtractor={ item => `contato-${item.id}`}
        />
      </View>
    </View>
  );
}
