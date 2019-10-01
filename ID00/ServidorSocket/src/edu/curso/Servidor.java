package edu.curso;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Servidor {
	private final static int PORTA = 20000;
	private ServerSocket servidor = null;
	private Socket cliente = null;
	public Servidor() throws IOException { 
		System.out.println("Servidor esta sendo iniciado");
		servidor = new ServerSocket(PORTA);
		System.out.println("Servidor iniciado com sucesso");
	}
	
	public void esperar() throws IOException { 
		cliente = servidor.accept();
		System.out.println("Cliente conectado com sucesso");
	}
	
	public void fecharServidor() throws IOException { 
		servidor.close();
	}
	
	public void mandarMensagem(String msg) throws IOException {
		OutputStream out = cliente.getOutputStream();
		out.write(msg.getBytes());
		out.flush();
	}
	
	public void recebeTextos() throws IOException {
		boolean sair = false;
		InputStream in = cliente.getInputStream();
		while (!sair) { 
			int i = in.read();
			if (i == 27) { 
				sair = true;
			} else { 
				System.out.print((char)i);
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		Servidor srv = new Servidor();
		srv.esperar();
		srv.mandarMensagem("Ola bem vindo ao servidor Java\r\n");
		srv.mandarMensagem("O que você digitar aparecer na tela do servidor\r\n");
		srv.recebeTextos();
	}

}
