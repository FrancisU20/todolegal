async function obtenerDireccionIP() {
  try {
    const response = await fetch("https://ipinfo.io/json");
    if (!response.ok) {
      throw new Error("No se pudo obtener la dirección IP del cliente");
    }
    const ipInfo = await response.json();
    return ipInfo.ip;
  } catch (error) {
    console.error("Error al obtener la dirección IP:", error);
    return null;
  }
}

// Método para enviar datos al webhook
async function enviarDatosAlWebhook(ip) {
  const data = {
    nombre: "Francisco Ulloa",
    "hora-local": new Date().toLocaleString(),
    ip: ip, // Utilizamos la dirección IP proporcionada
  };

  try {
    const response = await fetch(
      "https://webhook.site/4008ee2d-cde5-44b9-b3c0-2773746625db",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      }
    );

    if (response.ok) {
      console.log("Datos enviados con éxito");
    } else {
      console.error("Error al enviar datos al webhook");
    }
  } catch (error) {
    console.error("Error al enviar datos:", error);
  }
}

export { obtenerDireccionIP, enviarDatosAlWebhook };
