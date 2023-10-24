export default {
    data() {
      return {
        uploadedImages: [],
        imageSizeExceeded: false,
      };
    },
    methods: {
      handleImageUpload(event) {
        const files = event.target.files;
        for (let i = 0; i < files.length; i++) {
          const file = files[i];
          if (file.size <= 5000000) {
            const reader = new FileReader();
            const name = file.name.length > 25 ? file.name.substring(0, 25) + '...' : file.name;
            reader.onload = (e) => {
              this.uploadedImages.push({
                src: e.target.result,
                name: name,
              });
            };
            reader.readAsDataURL(file);
            this.imageSizeExceeded = false;
          } else {
            this.imageSizeExceeded = true;
          }
        }
      },
      removeImage(index) {
        this.uploadedImages.splice(index, 1);
        this.imageSizeExceeded = false;
      },
    },
  };