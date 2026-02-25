// src/types/index.ts
export interface Sale {
    id: number;
    order_date: string;
    product_name: string;
    category: string;
    region: string;
    quantity: number;
    sales_amount: number;
    profit: number;
    display_date?: string;
}

export interface DashboardStats {
    total_revenue: number;
    total_profit: number;
    average_profit: number;
    total_orders: number;
}