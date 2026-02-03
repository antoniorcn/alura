import { ScrollView, Text, View } from 'react-native';
import { estilos } from './styles/estilos';
import Contato from './Contato';

interface AppVideo2_3_1Props { 

}

export const AppVideo2_3_1 : React.FC<AppVideo2_3_1Props> = () => {
  
  const contatos : Contato[] = [
    {id: 1, nome:"João Silva", telefone: "(11) 1111-1111", email: "joao@teste.com"},
    {id: 2, nome:"Maria Silva", telefone: "(11) 2222-2222", email: "maria@teste.com"},
    {id: 3, nome:"Jose Santos", telefone: "(11) 3333-3333", email: "jose@teste.com"},
    {id: 4, nome:"Marta Gonçalves", telefone: "(11) 4444-4444", email: "marta@teste.com"}
  ];

  const lista = [];
  for ( let i = 0; i < 2000; i++) { 
    const contato = contatos[ i % 4 ];
    lista.push( { ...contato } );
  }

  const listaVisual = lista.map( item => {return (
      <View style={estilos.secondaryContainer}>
        <Text style={estilos.title}>{item.nome}</Text>
        <Text>Tel.: {item.telefone}</Text>
        <Text>{item.email}</Text>
      </View>
    ) }
  )

  return (
    <ScrollView style={{flex: 1}}>
      <Text>Elementos: {listaVisual.length}</Text>
      {listaVisual}
    </ScrollView>
  );
}