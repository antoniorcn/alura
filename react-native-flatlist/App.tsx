import { Text, View } from 'react-native';
import { estilos } from './styles/estilos';
import React from 'react';
import AppVideo5_3_1 from './AppVideo5_3_1';

export default function App() {
  return (
    <View style={estilos.container}>
      <Text>5.3.1</Text>
      <AppVideo5_3_1/>
    </View>
  );
}