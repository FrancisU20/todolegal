<template>
  <div class="container-fluid">
    <nav class="navbar navbar-expand-lg bg-white">
      <a class="navbar-brand logo" href="#">
        <img src="../assets/logo.png" alt="Logo" class="logo" />
      </a>
      <div class="spacer-navbar"></div>
      <button
        class="navbar-toggler d-block border-0 ml-auto"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
      >
        <font-awesome-icon :icon="['fas', 'bars']" class="blue-icon" />
      </button>
    </nav>

    <!-- Contenedor con Bootstrap -->
    <div class="container mt-4">
      <!-- Primera fila de tarjetas con Bootstrap -->
      <div class="card d-none d-md-block" style="border: none">
        <div class="card-body">
          <div class="row">
            <div class="col-3 menu-title">Firma de documentos</div>
            <div class="col-3 plain-text">
              <div class="circle-icon">
                <font-awesome-icon :icon="['fas', '1']" class="blue-icon" />
              </div>
              Cargar Documento
            </div>
            <div class="col-3 plain-text">
              <div class="circle-icon">
                <font-awesome-icon :icon="['fas', '2']" class="blue-icon" />
              </div>
              Indicar firmantes
            </div>
            <div class="col-3 plain-text">
              <div class="circle-icon">
                <font-awesome-icon :icon="['fas', '3']" class="blue-icon" />
              </div>
              Personalizaciones Opcionales
            </div>
          </div>
        </div>
      </div>

      <!-- Segunda fila de tarjetas con Bootstrap -->
      <div class="row mt-4">
        <div class="col-md-6">
          <div class="card h-100" style="border: none">
            <div class="card-body">
              <h5 class="title-video">¿Cómo funciona?</h5>
              <img
                class="video img-fluid"
                src="../assets/home.png"
                alt="Imagen"
              />
              <p class="card-text video-subtitle d-none d-md-block">
                Este es un servicio gratuito de
                <span class="link">todolegal</span>
              </p>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <div class="card" style="border: none">
            <div class="card-body">
              <h5 class="upload-image-title">Carga de Documentos</h5>
              <h5 class="upload-image-subtitle">
                Sube tus documentos y ordénalos
              </h5>
              <div class="upload-card">
                <div v-if="uploadedImages.length > 0" class="uploaded-images">
                  <div
                    v-for="(image, index) in uploadedImages"
                    :key="index"
                    class="uploaded-image"
                  >
                    <div class="card border-0 mb-2 w-100 mx-auto p-1">
                      <div class="image-details">
                        <font-awesome-icon
                          icon="bars"
                          class="image-icon"
                        ></font-awesome-icon>
                        <div class="image-icon">|</div>
                        <span class="image-name">{{ image.name }}</span>
                        <div class="image-icon"></div>
                        <div class="image-icon">|</div>
                        <font-awesome-icon
                          icon="trash-can"
                          @click="removeImage(index)"
                          class="image-icon"
                          style="cursor: pointer"
                        ></font-awesome-icon>
                      </div>
                    </div>
                  </div>
                  <div class="card border-0 w-100 mx-auto p-1">
                    <div class="image-details">
                      <label for="fileInput" class="image-icon">
                        <input
                          type="file"
                          id="fileInput"
                          @change="handleImageUpload"
                          multiple
                          style="display: none"
                        />
                        <font-awesome-icon
                          icon="plus"
                          style="cursor: pointer"
                        ></font-awesome-icon>
                      </label>
                      <div class="image-icon">|</div>
                      <label class="link-upload" for="fileInput"
                        >Añadir más documentos</label
                      >
                      <div class="image-icon">|</div>
                      <div class="column">
                        <p class="mb-0 text-primary font-weight-bold">5 Max.</p>
                        <p class="mb-0 text-primary font-weight-bold">10 Mb.</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div v-else>
                  <img
                    class="upload-image"
                    src="../assets/upload.png"
                    alt="Imagen"
                  />
                  <p class="upload-card-subtitle">
                    Arrastra y suelta tus documentos aquí
                    <label for="fileInput" class="link-upload"
                      >o Buscar Archivo</label
                    >
                    <input
                      type="file"
                      id="fileInput"
                      @change="handleImageUpload"
                      multiple
                      style="display: none"
                    />
                  </p>
                </div>
              </div>
              <h5 class="warning-text">
                Solo se admite archivos en formato PDF
              </h5>
              <div class="spacer"></div>
              <div>
                <button class="btn btn-primary w-50" @click="enviarDatosConDireccionIP">
                  Siguiente
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import DashboardPage from "@/components/DashboardPage.js";
import {
  obtenerDireccionIP,
  enviarDatosAlWebhook,
} from "@/services/ApiService";

export default {
  mixins: [DashboardPage],
  methods: {
    async enviarDatosConDireccionIP() {
      const ip = await obtenerDireccionIP();
      if (ip) {
        await enviarDatosAlWebhook(ip);
      }
    },
  },
};
</script>

<style>
@import url("@/assets/style.css");
</style>
