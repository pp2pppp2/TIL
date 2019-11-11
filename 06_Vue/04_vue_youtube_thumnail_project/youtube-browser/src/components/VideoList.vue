<template>
  <ul class="col-lg-4 list-group">
    <video-listitem 
    v-for="video in videos" 
    :video='video' 
    :key="video.etag"
    @videoSelect="onVideoSelect"
    >
    </video-listitem>
  </ul>
</template>

<script>
import VideoListitem from './VideoListitem'

export default {
  name:'VideoList',
  components:{
    VideoListitem,
  },
  props:{
    videos:{
      type : Array,
      required : true,
    }
  },
  methods:{
    onVideoSelect(video){
      this.$emit('videoSelect', video)
    }
  },
  
}
</script>

<style>

</style>