<template>
    <div class="p-6 max-w-3xl mx-auto">
      <n-input
        v-model:value="query"
        placeholder="검색어를 입력하세요"
        @keyup.enter="search"
        class="mb-4"
      />
      <n-button type="primary" @click="search">검색</n-button>
  
      <div v-if="results.length" class="mt-6 space-y-4">
        <ResultCard
          v-for="item in results"
          :key="item.id"
          :item="item"
        />
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import ResultCard from '@/components/ResultCard.vue'
  
  const query = ref('')
  const results = ref([])
  
  const search = async () => {
    if (!query.value.trim()) {
    console.warn("검색어를 입력하세요.")
    return
    }

    try {
      const res = await fetch(`/api/search?q=${encodeURIComponent(query.value)}&top_k=3`)
      const data = await res.json()
      results.value = data.results
    } catch (e) {
      console.error("API 요청 실패:", e)
    }
  }
  </script>
  