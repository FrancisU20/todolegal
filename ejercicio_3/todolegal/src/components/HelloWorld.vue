<template>
  <div>
    <!-- Barra de navegación con icono -->
    <nav class="navbar navbar-expand-lg navbar-bg">
      <a class="navbar-brand logo" href="#">
        <img src="../assets/logo.png" alt="Logo" class="logo" />
      </a>
      <button class="navbar-toggler" type="button">
        <font-awesome-icon :icon="['fas', 'bars']" />
      </button>

      <!-- Contenido del menú que se ocultará en pantallas más grandes -->
      <div class="collapse navbar-collapse d-lg-none d-xl-none">
        <!-- Aquí coloca tus elementos de menú -->
      </div>
    </nav>

    <!-- Contenedor con Bootstrap -->
    <div class="container mt-4">
      <!-- Primera fila de tarjetas con Bootstrap -->
      <div class="card" style="border: none">
        <div class="card-body">
          <div class="row">
            <div class="col-3 menu-title">
              <i><font-awesome-icon :icon="['fas', 'circle']" /></i>
              Firma de documentos
            </div>
            <div class="col-3 plain-text">
              <i><font-awesome-icon :icon="['fas', 'circle']" /></i>
              <font-awesome-icon :icon="['fas', '1']" /> Cargar Documento
            </div>
            <div class="col-3 plain-text">
              <i><font-awesome-icon :icon="['fas', 'circle']" /></i>
              <font-awesome-icon icon="fa-solid fa-circle-2" /> Indicar
              firmantes
            </div>
            <div class="col-3 plain-text">
              <i><font-awesome-icon :icon="['fas', 'circle']" /></i>
              <font-awesome-icon :icon="['fas', '3']" /> Personalizaciones
              Opcionales
            </div>
          </div>
        </div>
      </div>

      <!-- Segunda fila de tarjetas con Bootstrap -->
      <div class="row mt-4">
        <div class="col-md-6">
          <div class="card" style="border: none">
            <div class="card-body">
              <h5 class="title-video">¿Cómo funciona?</h5>
              <img
                class="video img-fluid"
                src="../assets/home.png"
                alt="Imagen"
              />
              <p class="card-text video-subtitle">
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
                <div>
                  <img
                    class="upload-image"
                    src="../assets/upload.png"
                    alt="Imagen"
                  />

                  <p class="upload-card-subtitle">
                    Arrastra y suelta tus documentos aquí
                    <label for="fileInput" class="link">o Buscar Archivo</label>
                    <input type="file" id="fileInput" style="display: none" />
                  </p>
                </div>
              </div>
              <h5 class="warning-text">Solo se admite archivos en formato PDF</h5>
              <div class="spacer"></div>
              <button class="btn btn-primary mt-3">Siguiente</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
@import url("@/assets/style.css");
</style>
