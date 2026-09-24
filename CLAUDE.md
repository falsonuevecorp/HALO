# HALO — tema de Shopify

Este repo es el tema vivo de **hellohalo.us**.

## Cómo se publica: por GitHub, no por CLI

El tema **`HALO/main`** está conectado a este repositorio (rama `main`). **Un `git push origin main`
es el despliegue.** No hace falta el CLI y no se debe usar: escribe directo sobre el tema, lo
desincroniza de la rama y deja la integración trabada.

```bash
git add -A && git commit -m "..." && git push origin main
```

El despliegue tarda un par de minutos. Para comprobar que llegó, buscar en el HTML vivo algo que
solo exista en el commit nuevo:

```bash
curl -s "https://hellohalo.us/products/atacama-band%C2%AE?cb=$RANDOM" | grep -c "<marca del cambio>"
```

Si no llega, mirar **Tienda online → Temas**: cuando la sincronización falla, Shopify muestra un
aviso de conflicto ahí.

## Tienda

| | |
|---|---|
| Dominio público | `hellohalo.us` |
| Handle del admin | `hellohalocl` |
| `Shopify.shop` interno | `motosportcl-5asgzrqx.myshopify.com` |
| `shopId` | `99687989555` |
| Tema vivo | `HALO/main` · `188120564019` |

Los dos handles existen: la tienda se renombró y el admin usa `hellohalocl` mientras el objeto
`Shopify.shop` del storefront sigue devolviendo el original. **Si alguna vez hay que usar el CLI, el
error *"you don't have access to this dev store"* casi siempre significa que la sesión está abierta
con la cuenta equivocada, no que el handle esté mal.** Armando tiene varias tiendas (Motosport,
Smilu Ve) y ese mensaje despista.

## Código que no se toca

- **Microsoft Clarity** vive al principio del `<head>` en `layout/theme.liquid`, proyecto
  `yjudh567uu`, con un comentario "NO BORRAR". Solo puede haber un tag: dos se pisan entre sí.
- **No hay código de Meta en el tema.** El píxel entra por el canal de Facebook & Instagram, así que
  un push no lo puede borrar. Lo que sí rompe la configuración es cambiar el texto o las clases de un
  botón, porque el Event Setup Tool los usa como ancla.
