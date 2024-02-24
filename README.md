PIK - API
====================

## Requerimientos

* Python 3.5+
* Pip 3  

- - -

## Ambientación

1. Install Python 3.5+

2. Install Pip 3

3. Install virtualenv  
Se usa para crear ambientes virtuales y ejecutar la versión de Python requerida

4. Clonar el proyecto  

5. Activar el ambiente virtual  
$ source env/bin/activate
  Windows:
C:/path_to_the_folder/> env/Project_name/Scripts/activate.bat

6. Instalar las librerías requeridas por el proyecto  
$ pip3 install -r requirements.txt

7. Configurar conexión a base de datos (MySQL)  
/sistema_fcc_api/my.cnf

8. Crear la base de datos y aplicar las migraciones  
$ python3 manage.py makemigrations sistema_fcc_api  
$ python3 manage.py migrate  


9. Cargar todos los fixtures en el orden en que están numerados. Ejemplo:  
$ ./manage.py loaddata fixtures/1initial_data.json
$ ./manage.py loaddata fixtures/2authgroup.json
$ ./manage.py loaddata fixtures/3user.json
etc..

10. Crear un django administrator (IMPORTANTE)  
$ python3 manage.py createsuperuser --email admin@admin.com --username admin  
(Console input) PASSWORD: XXXXXX

11. Correr el servidor  
 python3 manage.py runserver  

IMPORTANT: Initial data, requiered for the project. Run once the database was created.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  -

## API Contract (postman)

https://www.getpostman.com/collections/######################

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  -

## Despliegue en producción - Google App Engine

1. Generar los archivos estáticos de django (Solo se requiere en el primer deploy)  
$ python3 manage.py collectstatic

2. Conectarse a la BD de prod mediante un proxy (Previamente instalar sdk de google cloud)    
$ ./cloud_sql_proxy -instances="whatsoporte:us-west2:stgwhatsoport-mysql"=tcp:3307

3. Configurar en el archivo my.cnf la conexión hacia esta BD  

4. Aplicar las migraciones del proyecto

5. Configurar en el archivo settings.py la conexión a la BD de google cloud (esta comentada)  

6. Ejecutar el comando de publicación  
$ gcloud app deploy -v {ULTIMA_VERSION_DESPLEGADA}  

7. En caso de haber desplegado el API en un nuevo App Engine, se requiere actualizar la URL del API en el servicio de Chat API  
Este paso se requiere para que chat api pueda enviar los nuevos mensajes al web hook (link del nuevo API)

## JSONs dinamicos

Muchas funcionalidades de Center residen en objetos JSON que se guardan como texto en la BD. Estos son:

# Eventos: Atributos y configuración principal del evento

atributos_json: Lista los atributos visuales y de flujo de frontend del evento
Ej:
{
	"website": "https://www.bim.mx/",
	"icon_url": "https://cdnconventio.b-cdn.net/bim-foro-2021/assets/icono.png",
	"logo": "https://cdnconventio.b-cdn.net/bim-foro-2021/assets/logo.png",
	"color_primario": "#FFFFFF",
	"color_secundario": "#FFFFFF",
	"color_terciario": "#34B261",
	"font_color_titulos": "#064442",
	"font_name_titulos": "Montserrat",
	"font_color_default": "#000000",
	"boton_color_default": "#34B261",
	"font_name_default": "Montserrat",
	"menu_color": "#FFFFFF",
	"registro":{
		"bg": "https://cdnconventio.b-cdn.net/bim-foro-2021/assets/bg.jpg",
		"cupo": 1000,
		"dim_logo":{
			"width": "80%",
			"height": "60%"
		}
	},
	"warmup":{
		"loop": "https://cdnconventio.b-cdn.net/bim-foro-2021/videos/BIM_video_loop2.m4v"
	},
	"rutas":{
		"entrypoint":"registro",
		"pre_evento": {
			"anonimo": "registro",
			"usuario": "warm-up/loop"
		},
		"en_evento": {
			"anonimo": "registro",
			"usuario": "sala/foro"
		},
		"post_evento": "gracias"
	}
}

config_json: Contiene las llaves de configuracion especificas de un evento
Ej:
{
	"dominio": "localhost",
	"host_token": "host",
	"enviar_confirmacion_registro": true,
	"email_from": "BIM Foro 2021 <info@conventio.co>",
	"link_frontend": "http://bimforo2021.local:4200",
	"requiere_invitacion": false,
	"utc_gmt": "-6",
	"twilio_account_sid": "AC1bd0ba400b2d64c2e5becdf9ed2524ba",
	"twilio_auth_token": "99f637b75c63789cadce3d4adc87a5ca",
	"twilio_api_key": "SKad01c6e38694803bbb7e8d74d2020444",
	"twilio_api_secret": "QxhzBRSdUBEBu3sy4CLsUydIkW7biyTW",
	"twilio_service_sid": "ISd12c72a5a8154399b006aea6e760db28"
}

# SALAS: Cada sala tiene un contexto_json con los contenidos, como pueden ser:
- Livestream via zoom
{
	"plataforma": "zoom",
	"zoom":{
		"meeting_id": 99362247830,
		"meeting_password": "123456",
		"api_key": "sl_qg_MrSB2RHcb8mT-QmQ",
		"url": "https://zoom.bimforo2021.com.mx"
	},
	"saludo": "\u00a1Bienvenidos!",
	"texto_boton_ingreso": "Ingresa al foro",
	"chat": {
		"activo": true,
		"url": "https://chat.bimforo2021.com.mx"
	},
	"encuestas": false
}

- Livestream via youtube live
{
	"plataforma": "youtube",
	"youtube":{
		"video_url": "https://www.youtube.com/embed/-hkmrxy-C8k?start=1469"
	},
	"instrucciones": "Puedes dar DOBLE CLICK en el video para verlo en pantalla completa",
	"saludo": "\u00a1Bienvenidos!",
	"texto_boton_ingreso": "Ingresa al auditorio",
	"chat": {
		"activo": false
	},
	"encuestas": false,
	"interacciones": []
}

- Falso(s) en vivo
{
	"plataforma": "video",
	"videos":[
		{
			"es_default": true,
			"slug": "espanol",
			"nombre": "Español",
			"video_url": "https://cdnconventio.b-cdn.net/herbalife-seminario-2021/videos/falso_en_vivo_test.mp4",
			"duracion_segundos": 1168,
			"fecha_inicio": "2020-12-18 15:48:00 +0000",
			"fecha_fin": "2020-12-18 16:00:00 +0000"
		},
		{
			"slug": "english",
			"nombre": "English",
			"video_url": "https://cdnconventio.b-cdn.net/herbalife-seminario-2021/videos/falso_en_vivo_test_2.mp4",
			"duracion_segundos": 1168,
			"fecha_inicio": "2020-12-18 15:48:00 +0000",
			"fecha_fin": "2020-12-18 16:00:00 +0000"
		}
	],
	"saludo": "\u00a1Bienvenidos!",
	"texto_boton_ingreso": "Ingresa al auditorio",
	"chat": {
		"activo": false
	},
	"encuestas": false,
	"interacciones": []
}

# INTERACTIVOS: La tabla de interactivos tendrá una entrada por cada uno, y a su vez cada entrada su contexto_json con configuraciones de lógica y contenidos
Los interactivos disponibles hasta ahora son:

- Video post (subir imagen o video para recibir likes):
{
    "tipo_interactivo": "video_post",
    "slug": "cadena_musical",
    "nombre": "Cadena Musical 'Resistiré'",
    "warmup": true,
    "main": false,
    "fecha_inicio": "2020-12-15 09:00",
    "tutorial_url": "https://cdnconventio.b-cdn.net/cie-mensaje-2020/videos/RESISTIRE_CIE.mp4",
    "icon":"https://cdnconventio.b-cdn.net/cie-mensaje-2020/assets/cadena_musical.png",
    "instrucciones":{
        "descripcion": "Sube una parte de la canción 'Resistiré' acompañada de elementos creativos.",
        "links":[
            {
                "url": "https://open.spotify.com/album/5xl9aTPziZye5Jy5fGsyPh?si=Q7fvwVCTQW-MOQriyOL-FQ",
                "descripcion": "Escúchala en Spotify"
            },
            {
                "url": "https://music.apple.com/us/album/resistir%C3%A9-feat-aida-cuevas-arath-herce-axel-mu%C3%B1iz-belinda/1508030466",
                "descripcion": "Escúchala en Apple Music"
            },
            {
                "url": "https://www.youtube.com/watch?v=uBGlv05JUJI",
                "descripcion": "Véla en Youtube"
            }
        ]
    }
}

- Adivina la canción (colaborativo, dos compiten por adivinar el nombre de una canción al escuchar el audio):

{
        "tipo_interactivo": "adivina_cancion",
        "slug": "adivina_cancion",
        "nombre": "Adivina la canción",
        "warmup": false,
        "main": true,
        "fecha_inicio": "2020-12-11 08:00",
        "icon": "https://storage.googleapis.com/cocacola2020/assets/adivina_cancion_icon.png",
        "max_jugadores": 2,
        "canciones": [
            {
                "id": 1,
                "audio": "https://storage.googleapis.com/cocacola2020/adivina_cancion/Maluma_Hawai(Version_con_cantante)_10431219.mp3",
                "opciones": [
                    {
                        "id": 1,
                        "nombre": "Hawái",
                        "isCorrect": true,
                        "puntos": 100
                    },
                    {
                        "id": 2,
                        "nombre": "No Hay Nadie Más ",
                        "isCorrect": false
                    },
                    {
                        "id": 3,
                        "nombre": "Caramelo",
                        "isCorrect": false
                    },
                    {
                        "id": 4,
                        "nombre": "Crazy Little Thing Called Love",
                        "isCorrect": false
                    }
                ]
            }
        ]
}

- 100 mexicanos dijeron (colaborativo, dos compiten por adivinar qué contestaron más mexicanos a cierta pregunta):

{
    "tipo_interactivo": "100_mexicanos_dijeron",
    "slug": "100_mexicanos_dijeron",
    "nombre": "100 mexicanos dijeron",
    "warmup": false,
    "main": true,
    "fecha_inicio": "2020-12-11 08:00",
    "icon": "https://storage.googleapis.com/cocacola2020/assets/100_mexicanos_dijeron_icon.png",
    "max_jugadores": 2,
    "preguntas": [
        {
            "id": 1,
            "pregunta": "Menciona algo opuesto a la libertad",
            "opciones": [
                {
                    "id": 1,
                    "nombre": "Esclavitud",
                    "show": false,
                    "puntos": 40
                },
                {
                    "id": 2,
                    "nombre": "Encierro",
                    "show": false,
                    "puntos": 30
                },
                {
                    "id": 3,
                    "nombre": "Prisión",
                    "show": false,
                    "puntos": 20
                },
                {
                    "id": 4,
                    "nombre": "Opresión",
                    "show": false,
                    "puntos": 10
                }
            ],
            "respuestas": [
                {
                    "id": 1,
                    "nombre": "Esclavitud",
                    "correcta": true,
                    "active": true
                },
                {
                    "id": 2,
                    "nombre": "Encierro",
                    "correcta": true,
                    "active": true
                },
                {
                    "id": 3,
                    "nombre": "Prisión",
                    "correcta": true,
                    "active": true
                },
                {
                    "id": 4,
                    "nombre": "Opresión",
                    "correcta": true,
                    "active": true
                },
                {
                    "id": 5,
                    "nombre": "Independencia",
                    "correcta": false,
                    "active": true
                },
                {
                    "id": 6,
                    "nombre": "Liberación",
                    "correcta": false,
                    "active": true
                },
                {
                    "id": 7,
                    "nombre": "Libramiento",
                    "correcta": false,
                    "active": true
                },
                {
                    "id": 8,
                    "nombre": "Emancipación",
                    "correcta": false,
                    "active": true
                },
                {
                    "id": 9,
                    "nombre": "Dominio",
                    "correcta": false,
                    "active": true
                },
                {
                    "id": 10,
                    "nombre": "Sometimiento",
                    "correcta": false,
                    "active": true
                },
                {
                    "id": 11,
                    "nombre": "Servidumbre",
                    "correcta": false,
                    "active": true
                },
                {
                    "id": 12,
                    "nombre": "Dependencia",
                    "correcta": false,
                    "active": true
                }
            ]
        }
    ]
}

# Encuestas: Se lanzan a una sala en tiempo real

{
	"pregunta": "\u00bfQu\u00e9 canci\u00f3n de Sebastian Yatra quieres escuchar?",
	"opciones": [{
		"opcion": "1",
		"texto": "Traicionera"
	}, {
		"opcion": "2",
		"texto": "Te vas"
	}, {
		"opcion": "3",
		"texto": "Despecho"
	}, {
		"opcion": "4",
		"texto": "El amor"
	}]
}


## JSON del POSTMAN (API spec)

{
	"info": {
		"_postman_id": "fd02ab4a-3190-41f7-89db-81647e4ee7ab",
		"name": "Center API",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "Auth",
			"item": [
				{
					"name": "Login con permalink",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{http}}://{{host}}/token/permalink/VSYP5350/bim-foro-2021",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"token",
								"permalink",
								"VSYP5350",
								"bim-foro-2021"
							]
						}
					},
					"response": []
				},
				{
					"name": "Login con acceso unico y dominio",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{http}}://{{host}}/token/acceso_unico/HOZV4715?dominio=localhost",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"token",
								"acceso_unico",
								"HOZV4715"
							],
							"query": [
								{
									"key": "dominio",
									"value": "localhost"
								}
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "HOST",
			"item": [
				{
					"name": "Purgar cache de un evento",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "POST",
						"header": [],
						"url": {
							"raw": "{{http}}://{{host}}/host/evento/herbalife-seminario-2021/cache/{{host_token}}",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"host",
								"evento",
								"herbalife-seminario-2021",
								"cache",
								"{{host_token}}"
							]
						}
					},
					"response": []
				},
				{
					"name": "Apagar/prender interacciones de una sala",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{http}}://{{host}}/host/salas/1/interaccion/control/host",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"host",
								"salas",
								"1",
								"interaccion",
								"control",
								"host"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Eventos",
			"item": [
				{
					"name": "Obtener el detalle de un evento",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{http}}://{{host}}/eventos/bim-foro-2021",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"eventos",
								"bim-foro-2021"
							],
							"query": [
								{
									"key": "tyco",
									"value": "1",
									"disabled": true
								}
							]
						}
					},
					"response": []
				},
				{
					"name": "Obtener el aforo actual de un evento",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{http}}://{{host}}/eventos/bim-foro-2021/aforo",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"eventos",
								"bim-foro-2021",
								"aforo"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Chat",
			"item": [
				{
					"name": "Obtener signature del chat",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"id_user\": 261\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{http}}://{{host}}/chat/bim-foro-2021/signature",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"chat",
								"bim-foro-2021",
								"signature"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Registro",
			"item": [
				{
					"name": "Registrarse para un evento",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "nombre_completo",
									"value": "Felix 501",
									"type": "text"
								},
								{
									"key": "email",
									"value": "felix+501@inflexionsoftware.com",
									"type": "text"
								},
								{
									"key": "foto_perfil",
									"value": null,
									"type": "file",
									"disabled": true
								},
								{
									"key": "perfil_contexto_json",
									"value": "{}",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{http}}://{{host}}/usuarios/registro/bim-foro-2021",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"usuarios",
								"registro",
								"bim-foro-2021"
							]
						}
					},
					"response": []
				},
				{
					"name": "Registro masivo (excel) a un evento",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "token",
									"value": "jgk78shdjngftiao34_jek$!!jks",
									"type": "text"
								},
								{
									"key": "usuarios",
									"value": null,
									"type": "file"
								}
							]
						},
						"url": {
							"raw": "{{http}}://{{host}}/registro/masivo/herbalife-seminario-2021",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"registro",
								"masivo",
								"herbalife-seminario-2021"
							]
						}
					},
					"response": []
				},
				{
					"name": "Envio masivo (invitaciones) de un evento",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "token",
									"value": "jgk78shdjngftiao34_jek$!!jks",
									"type": "text"
								},
								{
									"key": "usuarios",
									"value": null,
									"type": "file"
								},
								{
									"key": "tipo_envio",
									"value": "invitacion_registro",
									"type": "text"
								},
								{
									"key": "email_bcc",
									"value": "berliner@inflexionsoftware.com",
									"type": "text",
									"disabled": true
								},
								{
									"key": "subject",
									"value": "Mensaje de Fin de Año CIE 2020",
									"type": "text"
								}
							],
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{http}}://{{host}}/registro/envios/cie-mensaje-2020",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"registro",
								"envios",
								"cie-mensaje-2020"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Me",
			"item": [
				{
					"name": "Obtener mi info (del usuario logeado)",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{token}}",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{http}}://{{host}}/me/bim-foro-2021",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"me",
								"bim-foro-2021"
							]
						}
					},
					"response": []
				},
				{
					"name": "Aprobar/agregar un dispositivo para un usuario",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"sistema_operativo\": \"MacOS\",\n    \"navegador\": \"Chrome\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{http}}://{{host}}/me/cocacola2020/dispositivo",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"me",
								"cocacola2020",
								"dispositivo"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Salas",
			"item": [
				{
					"name": "Obtener detalle de una sala por slug",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{token}}",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{http}}://{{host}}/eventos/herbalife-seminario-2021/salas/seminario",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"eventos",
								"herbalife-seminario-2021",
								"salas",
								"seminario"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Notificaciones",
			"item": [
				{
					"name": "Envio masivo de mails para usuarios de un evento",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "tipo_envio",
									"value": "recordatorio_evento_rappi_1",
									"type": "text"
								},
								{
									"key": "usuarios",
									"value": null,
									"type": "file"
								},
								{
									"key": "email_bcc",
									"value": "",
									"type": "text",
									"disabled": true
								},
								{
									"key": "subject",
									"value": "¡Hoy es la Posada!",
									"type": "text"
								},
								{
									"key": "token",
									"value": "jgk78shdjngftiao34_jek$!!jks",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{http}}://{{host}}/eventos/cocacola2020/notificaciones/mail/masiva",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"eventos",
								"cocacola2020",
								"notificaciones",
								"mail",
								"masiva"
							]
						}
					},
					"response": []
				},
				{
					"name": "Envio de notificaciones a invitados de un evento (socket)",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"token\": \"8541b36390ddae8519d7752d1c9ac09e\",\n    \"message\":{\n        \"tipo\": \"mensaje\",\n        \"mensaje\": \"Amigo?\"\n    }\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://127.0.0.1:8080/messages/cocacola2020_notificaciones",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8080",
							"path": [
								"messages",
								"cocacola2020_notificaciones"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Partidas",
			"item": [
				{
					"name": "Iniciar una partida",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{token}}",
									"type": "string"
								}
							]
						},
						"method": "PUT",
						"header": [],
						"url": {
							"raw": "{{http}}://{{host}}/partidas/14/iniciar",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"partidas",
								"14",
								"iniciar"
							]
						}
					},
					"response": []
				},
				{
					"name": "Registrar un evento (algo que paso) en una partida)",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"evento_partida\":{\n        \"tipo\": \"respuesta\",\n        \"usuario_id\": 1,\n        \"respuesta_id\": 1\n    }\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{http}}://{{host}}/partidas/10/evento",
							"protocol": "{{http}}",
							"host": [
								"{{host}}"
							],
							"path": [
								"partidas",
								"10",
								"evento"
							]
						}
					},
					"response": []
				}
			]
		}
	]
}
