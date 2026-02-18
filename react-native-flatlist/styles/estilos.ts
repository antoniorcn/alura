import {StyleSheet} from 'react-native';
import material_theme from "./material-theme.json";


const tema = material_theme.schemes.light

const estilos = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor : tema.primaryContainer,
        color : tema.onPrimaryContainer,
        padding : 10,
        marginTop: 30,
        alignItems: 'stretch',
        justifyContent: 'center',
    },
    secondaryContainer: {
        backgroundColor : tema.secondaryContainer,
        color : tema.onSecondaryContainer,
        padding : 10,
        margin: 10,
        borderRadius: 15,
        borderColor: tema.secondary,
        borderWidth: 2
    },
    title : {
        fontSize: 16,
        fontWeight: "bold",
        color: tema.onSecondaryContainer
    },
    body : {
        fontSize: 12,
        fontWeight: "normal",
        color: tema.onSecondaryContainer       
    },
    textInput : { 
        backgroundColor: tema.surfaceDim,
        color : tema.onSurfaceVariant,
        borderRadius: 5,
        borderBottomWidth: 2,
        borderBottomColor: tema.onSurface
    },
    header: {
        backgroundColor: tema.onPrimary,
        padding: 30,
        alignItems: "center",
        color: tema.onPrimaryContainer
    },
    headerText: {
        fontSize: 32,
        fontWeight: "bold",
        color: tema.onPrimaryContainer
    },
    flatListContainer: {
        borderColor: tema.onSecondary,
        borderWidth: 3,
        marginBottom: 10
    },
    flatListSeparator: {
        marginHorizontal: 5,
        marginVertical: 10,
        borderTopWidth: 2,
        borderTopColor: tema.onSecondary
    },
    footer: {
        backgroundColor: tema.primary,
        padding: 20,
        alignItems: "flex-end",
    },
    footerText: {
        fontSize: 16,
        fontStyle: "italic",
        color: tema.onPrimaryContainer
    },
})
export { tema, estilos }