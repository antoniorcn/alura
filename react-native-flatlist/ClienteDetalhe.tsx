import { Text, View } from 'react-native';
import { estilos } from './styles/estilos';
import Contato from './Contato';

interface ContatoDetalheProps { 
  contato : Contato
}

const ContatoDetalhe : React.FC<ContatoDetalheProps> = ( { contato } ) => { 
  return (
    <View key={"item-"+ contato.id} style={estilos.secondaryContainer}>
      <Text style={estilos.title}>{contato.nome}</Text>
      <Text>{contato.telefone}</Text>
      <Text>{contato.email}</Text>
    </View>
  )
}

export default ContatoDetalhe;