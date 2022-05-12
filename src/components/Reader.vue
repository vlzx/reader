<script setup lang="ts">
import {onMounted} from "vue";
import translate from "../composables/youdao-translate";
import tokenize from "../composables/kuromoji";

onMounted(() => {
  const data = translate('寿司を食べたい')
  data.then(data => {
    if (data['errorCode'] == '0') {
      console.log(data['translation']);
    } else {
      console.log(data)
      // warning message
    }
  })
  setTimeout(() => {
    const tokens = tokenize('今日は')
    console.log(tokens)
  }, 1000)
})
</script>

<template>
  <div>Reader Page</div>
</template>

<style scoped>

</style>