<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import api from '../api';
import VueApexCharts from "vue3-apexcharts";
import type { Sale, DashboardStats } from '../types';

const sales = ref<Sale[]>([]);
const stats = ref<DashboardStats | null>(null);
const loading = ref(true);

// 1. GROUPEMENT DES DONNÉES (Pour éviter le graphique illisible)
const monthlySeries = computed(() => {
  const groups: { [key: string]: number } = {};
  
  sales.value.forEach(s => {
    const month = s.order_date.substring(0, 7); // Récupère "YYYY-MM"
    groups[month] = (groups[month] || 0) + s.sales_amount;
  });

  const sortedMonths = Object.keys(groups).sort();
  return [{
    name: 'Ventes Mensuelles',
    data: sortedMonths.map(m => ({ x: m, y: Math.round(groups[m]) }))
  }];
});

// 2. CONFIGURATION APEXCHARTS (Style Moderne)
const chartOptions = {
  chart: { 
    toolbar: { show: false },
    dropShadow: { enabled: true, top: 3, left: 2, blur: 4, opacity: 0.1 }
  },
  stroke: { curve: 'smooth', width: 3 },
  colors: ['#3b82f6'],
  dataLabels: { enabled: false }, // INDISPENSABLE : Enlève les étiquettes qui cachent tout
  xaxis: { type: 'datetime' },
  grid: { borderColor: '#f1f5f9' },
  fill: {
    type: 'gradient',
    gradient: { shadeIntensity: 1, opacityFrom: 0.4, opacityTo: 0.1 }
  }
};

const fetchData = async () => {
  try {
    const [salesRes, statsRes] = await Promise.all([
      api.get('sales/'),
      api.get('sales/stats/')
    ]);
    sales.value = salesRes.data;
    stats.value = statsRes.data;
  } finally {
    loading.value = false;
  }
};

onMounted(fetchData);
</script>

<template>
  <div class="min-h-screen bg-[#f3f4f9] p-4 lg:p-8">
    <div class="max-w-7xl mx-auto">
      
      <div class="flex flex-col md:flex-row md:items-center justify-between mb-8 gap-4">
        <h1 class="text-2xl font-bold text-slate-800">Web analytics dashboard</h1>
        <div class="flex gap-3">
          <button class="px-4 py-2 bg-slate-200 text-slate-700 rounded-lg font-medium hover:bg-slate-300 transition">Explore more</button>
          <button class="px-4 py-2 bg-[#2d1b69] text-white rounded-lg font-medium hover:bg-opacity-90 transition">Set up dashboard</button>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        <div class="bg-white p-3 rounded-lg border border-slate-200 text-slate-500 text-sm">May 1, 2025 - Jun 23, 2025</div>
        <div class="bg-white p-3 rounded-lg border border-slate-200 text-slate-500 text-sm">Session channel group</div>
        <div class="bg-white p-3 rounded-lg border border-slate-200 text-slate-500 text-sm">Device category</div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4 mb-8">
        <div class="bg-[#1a73e8] p-5 rounded-xl text-white shadow-md">
          <p class="text-xs uppercase opacity-80 font-bold">Total users</p>
          <p class="text-2xl font-bold mt-1">{{ sales.length }}</p>
        </div>
        <div class="bg-[#00a3cc] p-5 rounded-xl text-white shadow-md">
          <p class="text-xs uppercase opacity-80 font-bold">New users</p>
          <p class="text-2xl font-bold mt-1">101.1K</p>
        </div>
        <div class="bg-[#00c48c] p-5 rounded-xl text-white shadow-md">
          <p class="text-xs uppercase opacity-80 font-bold">Sessions</p>
          <p class="text-2xl font-bold mt-1">178.4K</p>
        </div>
        <div class="bg-[#eb5757] p-5 rounded-xl text-white shadow-md">
          <p class="text-xs uppercase opacity-80 font-bold">Purchases</p>
          <p class="text-2xl font-bold mt-1">{{ stats?.total_orders }}</p>
        </div>
        <div class="bg-[#9b51e0] p-5 rounded-xl text-white shadow-md">
          <p class="text-xs uppercase opacity-80 font-bold">Total revenue</p>
          <p class="text-2xl font-bold mt-1">${{ stats?.total_revenue }}</p>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
          <h3 class="font-bold text-slate-700 mb-6">Recent Daily Traffic</h3>
          <div v-if="loading" class="h-64 flex items-center justify-center italic text-slate-400">Chargement...</div>
          <VueApexCharts v-else type="area" height="300" :options="chartOptions" :series="monthlySeries" />
        </div>

        <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
          <h3 class="font-bold text-slate-700 mb-6">Weekly Traffic (Last 6 Months)</h3>
          <div v-if="loading" class="h-64 flex items-center justify-center italic text-slate-400">Chargement...</div>
          <VueApexCharts v-else type="bar" height="300" :options="{...chartOptions, colors: ['#0369a1']}" :series="monthlySeries" />
        </div>

      </div>

      <div class="mt-8 bg-white rounded-2xl shadow-sm border border-slate-100 overflow-hidden">
        <table class="w-full text-left">
          <thead class="bg-slate-50 text-slate-500 text-xs uppercase">
            <tr>
              <th class="px-6 py-4 font-bold">Produit</th>
              <th class="px-6 py-4 font-bold">Région</th>
              <th class="px-6 py-4 font-bold">Montant</th>
              <th class="px-6 py-4 font-bold">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100">
            <tr v-for="sale in sales.slice(0, 5)" :key="sale.id" class="text-sm hover:bg-slate-50 transition">
              <td class="px-6 py-4 font-medium">{{ sale.product_name }}</td>
              <td class="px-6 py-4">{{ sale.region }}</td>
              <td class="px-6 py-4 font-bold text-blue-600">{{ sale.sales_amount }} €</td>
              <td class="px-6 py-4">
                <button class="text-red-500 hover:underline">Supprimer</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

    </div>
  </div>
</template>