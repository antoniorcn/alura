import { Button, FlatList, ListRenderItemInfo, RefreshControl, ScrollView, Text, TextInput, View } from 'react-native';
import { estilos } from './styles/estilos';
import Contato from './Contato';
import { useEffect, useState } from 'react';
import { FontAwesome as Icon} from '@expo/vector-icons';
import axios, { AxiosResponse } from 'axios';


const api = axios.create( {baseURL: "https://fakerapi.it/api/v2"} )

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

const EmptyList = () => (
  <View style={[estilos.flatListContainer, {alignItems: "center"}]}>
    <Text style={estilos.headerText}>Não há elementos na lista</Text>
  </View>
);


export default function AppVideo5_2_1() {

  const contatos : Contato[] = [];

  const [lista, setLista] = useState<Contato[]>([...contatos]);
  const [atualizando, setAtualizando] = useState<boolean>(false);
  const [idCounter, setIdCounter] = useState<number>(0);

  const onRefresh = async () => {
    setAtualizando(true);
    console.log("Atualizando")
    api.get("/persons?_quantity=5")
    .then( ( response : AxiosResponse<any, any> )=>{
      console.log("Dados carregados...");
      console.log(response);
      const listaTemp = [...lista];
      for (const contato of response.data.data) {
        setIdCounter( 
          ( currentId ) => {
            listaTemp.push( { id: currentId, nome: `${contato.firstname} ${contato.lastname}`, telefone: contato.phone, email: contato.email  } );
            return currentId + 1;
          }
        );
      }
      setLista( listaTemp );
      setAtualizando(false);
    })
    .catch(( err : any ) => {
      console.log("Erro: ", err);
      setAtualizando(false);
    });
  }

  return (
    <FlatList   data={lista}
                initialNumToRender={10}
                maxToRenderPerBatch={10}
                windowSize={21}
                removeClippedSubviews={false}
                ListHeaderComponent={ListaHeader}
                ListFooterComponent={ListaFooter}
                ListEmptyComponent={EmptyList}
                refreshControl={<RefreshControl
                    refreshing={atualizando}
                    onRefresh={onRefresh}/>}
                renderItem={flatProps =><ContatoDetalhe {...flatProps} 
                                                        onEditar={()=>{}} 
                                                        onApagar={()=>{}}/>}
                keyExtractor={ item => `contato-${item.id}`}
    />
  );
}
