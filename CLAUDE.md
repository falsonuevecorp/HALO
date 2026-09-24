# HALO — tema de Shopify

Este repo es el tema vivo de **hellohalo.us**.

## Tienda

| | |
|---|---|
| Dominio público | `hellohalo.us` |
| Dominio de Shopify | **`motosportcl-5asgzrqx.myshopify.com`** |
| `shopId` | `99687989555` |
| Tema vivo | `188120564019` |

**El handle de la tienda NO es `hellohalocl`.** Esa tienda existe pero es otra y el CLI
responde "you don't have access to this dev store", lo que parece un problema de sesión y no lo es.
Para verificarlo sin adivinar:

```bash
curl -s https://hellohalo.us/ | grep -oE 'Shopify\.shop = "[^"]+"'
```

## Publicar

```bash
NPM_CONFIG_PREFIX=/Users/armandoluzardo/.npm-global ~/.npm-global/bin/shopify theme push \
  --store motosportcl-5asgzrqx --theme 188120564019 --allow-live \
  --only <archivo>
```

El prefijo `NPM_CONFIG_PREFIX` es obligatorio: sin él el CLI no encuentra su propia instalación.

Si pide login, abre el navegador con un código de verificación. **Hay que entrar con la cuenta
dueña de esta tienda**; con otra cuenta el login funciona pero el push falla con el mismo mensaje
de "dev store".

## Código que no se toca

- **Microsoft Clarity** vive al principio del `<head>` en `layout/theme.liquid`, proyecto
  `yjudh567uu`, con un comentario "NO BORRAR". Solo puede haber un tag: dos se pisan entre sí.
- **No hay código de Meta en el tema.** El píxel entra por el canal de Facebook & Instagram.
  Un push no lo puede borrar. Lo que sí rompe la configuración es cambiar el texto o las clases
  de un botón, porque el Event Setup Tool los usa como ancla.

Antes de empujar `layout/theme.liquid`, confirmar que el bloque de Clarity sigue ahí, y bajar
primero los cambios hechos a mano en el editor de temas en vez de sobrescribirlos.
