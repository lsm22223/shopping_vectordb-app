<template>
    <n-card>
      <template #header>
        {{ item.metadata.product_name }} ({{ item.metadata.brand }})
      </template>
  
      <div class="text-sm text-gray-700">{{ item.description }}</div>
  
      <ul class="mt-2 text-sm text-gray-600 space-y-1">
        <li>💰 가격: {{ formatPrice(item.metadata.price) }}</li>
        <li>⭐ 평점: {{ item.metadata.rating }} / 후기 {{ item.metadata.review_count }}개</li>
        <li>📦 재고 상태: {{ item.metadata.stock_status }}</li>
        <li>🗓️ 출시일: {{ item.metadata.release_date }}</li>
        <li>🏷️ 카테고리: {{ item.metadata.category }} / {{ item.metadata.subcategory }}</li>
        <li>🧩 특징: {{ item.metadata.feature_tags }}</li>
        <li>🔥 베스트셀러: {{ item.metadata.is_bestseller ? '✅ Yes' : '❌ No' }}</li>
        <li>📉 할인율: {{ item.metadata.discount_rate }}%</li>
      </ul>
  
      <div class="text-xs text-right text-gray-400 mt-2">
        🔁 Cosine 유사도: {{ item.cosine_similarity.toFixed(4) }}<br />
        🔢 L2 거리: {{ item.l2_distance.toFixed(4) }}
      </div>
    </n-card>
  </template>
  
  <script setup>
  defineProps({ item: Object })
  
  function formatPrice(val) {
    return `${val.toLocaleString()}원`
  }
  </script>
  