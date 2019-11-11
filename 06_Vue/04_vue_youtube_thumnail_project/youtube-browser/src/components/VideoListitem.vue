<template>
  <li @click="onVideoSelect" class="list-group-item">
    <img :src="thumbnailUrl" alt="youtube-thumbnail-image" class='mr-3'>
    <div class="media-body">
      {{ video.snippet.title }}
    </div>
  </li>
</template>

<script>
export default {
  name:'VideoListitem',
  props:{
    video:{
      type: Object,
      required: true,
    }
  },
  computed: {
    thumbnailUrl(){
      return this.video.snippet.thumbnails.default.url
    }
  },
  methods: {
    onVideoSelect() {
      this.$emit('videoSelect', this.video)
    }
  }
}
</script>

<style scoped>
  li {
    display: flex;
    cursor: pointer;
  }

  li:hover {
    background-color: #eee;
  }

</style>